from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from .models import Student

def validate_age(age):
    print(age)
    if age>25:
        raise ValidationError('%(age)s is not in range',params={'age':age})

class StudentReg(forms.Form):
    name=forms.CharField(
        max_length=16,
        # initial='Name',
        required=True,
        help_text='(name on aadhar)',
        widget=forms.TextInput,
        )
    
    email=forms.EmailField()

    age=forms.IntegerField(
        initial=18,
        required=False,
        validators=[validate_age]
        )
    
    phno = forms.CharField(
        label="phno Number",
        max_length=10, 
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="phno number must be entered "
            )
        ],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phno number'})
    )
 
    
    colors=(('red','Red'),('green','Green'),('blue','Blue'))
    
    fav_col=forms.ChoiceField(
        choices=colors,
        label="Choose your color"
    )

    pwd=forms.CharField(
        widget=forms.PasswordInput(),
        label='Password',
        required=True
        # disabled=True
        )
    
    confpwd=forms.CharField(
        widget=forms.PasswordInput(),
        label='Confim Password',
        required=True
        # disabled=True
        )


    def clean_age(self):
        age=self.cleaned_data.get('age')
        if age<18:
            raise ValidationError("Age should be more than 18")
        return age
    
    def clean(self):
        cleaned_data=super().clean()
        pwd=cleaned_data.get('pwd')
        confpwd=cleaned_data.get('confpwd')
        if pwd != confpwd:
            raise ValidationError('Passwords dont match')
        return cleaned_data
    
class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'course', 'phno', 'age', 'email','password']
 
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError('Name must contain only letters and spaces.')
        return name
 
    def clean_phno(self):
        phno = self.cleaned_data.get('phno')
        if not phno.isdigit() or len(phno) != 10:
            raise forms.ValidationError('Phone number must be exactly 10 digits.')
        return phno
 
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 17 or age > 100:
            raise forms.ValidationError('Age must be between 17 and 100.')
        return age
    
class StudentLogin(forms.Form):
    email=forms.EmailField()

    password=forms.CharField()