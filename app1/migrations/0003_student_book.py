# Generated by Django 5.0.1 on 2024-08-11 05:36

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[A-Za-Z]+$', 'Name should only have letters and spaces')])),
                ('course', models.CharField(max_length=50)),
                ('phno', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Invalid phone number (Exactly 10 digits)')])),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(18, 'Must be atleast 18'), django.core.validators.MinValueValidator(49, 'Must be under 50')])),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator('Email not valid!')])),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('publication_date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.author')),
            ],
        ),
    ]
