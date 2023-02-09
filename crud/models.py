from django.db import models

# Create your models here.
class Student(models.Model):
    gender_field=(
        ('male','Male'),
        ('female','Female')
    )
    language_field=(
        ('nepali','Nepali'),
        ('english','English'),
        ('chinese','Chinese')
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    gender = models.CharField(max_length=6,choices=gender_field)
    language = models.CharField(max_length=100,choices=language_field)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',blank=True,null=True)