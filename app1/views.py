from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import StudentReg
from django.core.exceptions import ValidationError
from .forms import StudentRegistrationForm,StudentLogin
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def test(request):
    print("Test function")
    return HttpResponse('<h1>Test page for app1</h1>')

def home(request):
    return render(request,'home.html',{"name":"Anto","age":17})

def user(request):
    val1=request.POST["name"]
    email=request.POST["email"]
    age=request.POST["age"]
    color=request.POST["fav_col"]
    phno=request.POST["phno"]
    return render(request,'user.html',{
        'name':val1,
        'email':email,
        'age':age,
        'color':color,
        'phno':phno
        })

def index(request):
    return render(request,'index.html')

def formdata(request):
    if request.method=="POST":
        fm=StudentReg(request.POST)
        if fm.is_valid():
            age=fm.cleaned_data["age"]
    
    return render(request,'registration.html',{'form':StudentReg()})


def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save()
            user = User.objects.create_user(username=student.email)
            user.set_password(form.cleaned_data['password'])  # Set the password for the user
            user.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')  
    else:
        form = StudentRegistrationForm()

    return render(request, 'stu_registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = StudentLogin(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                student = Student.objects.get(email=email)
                # Check if the password matches
                if student.password == password:
                    request.session['student_email'] = student.email
                    request.session['student_name'] = student.name
                    return redirect('/app1/user/')
                else:
                    messages.error(request, 'Invalid email or password.')
            except Student.DoesNotExist:
                messages.error(request, 'Invalid email or password.')
    else:
        form = StudentLogin()

    return render(request, 'login.html', {'form': form})

def user_page(request):
    student_email = request.session.get('student_email')
    if not student_email:
        return redirect('/app1/login/')  # Redirect to login if not logged in

    try:
        student_profile = Student.objects.get(email=student_email)
    except Student.DoesNotExist:
        return redirect('/app1/login/')  # Redirect to login if student not found

    context = {
        'name': student_profile.name,
        'email': student_profile.email,
        'age': student_profile.age,
        'course': student_profile.course,
    }
    return render(request, 'user.html', {'context':context})


def logout_view(request):
    request.session.flush()  
    return redirect('login')