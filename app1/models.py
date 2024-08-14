from django.db import models
from django.core.validators import RegexValidator,MinValueValidator,MaxValueValidator,EmailValidator

class Author(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)

class Book(models.Model):
    title=models.CharField(max_length=50)
    publication_date=models.DateField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)

class User(models.Model):
    name= models.CharField(
        max_length=25
    )
    age= models.IntegerField()

class Student(models.Model):
    # s_id=models.AutoField(primary_key=True)

    # course=models.ForeignKey(Course,on_delete=models.CASCADE)
    # # If the Course table is deleted then, course field in Student will also get deleted


    name=models.CharField(max_length=50,validators=[
        RegexValidator(r'^[A-Za-z]+$','Name should only have letters and spaces')
    ])

    course=models.CharField(max_length=50)

    phno=models.CharField(max_length=10,validators=[
        RegexValidator(r'^\d{10}$',"Invalid phone number (Exactly 10 digits)")
    ])

    password=models.CharField()

    age=models.PositiveIntegerField(validators=[
        MinValueValidator(18,"Must be atleast 18"),
        MaxValueValidator(49,"Must be under 50")
    ])

    email=models.EmailField(unique=True,validators=[
        EmailValidator('Email not valid!')
    ])

    def __str__(self):
        return f"[<{self.name}> <{self.course}>]"
