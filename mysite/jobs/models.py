from django.db import models
from django import forms

# Create your models here.

# class Person(models.Model):
#     email=models.EmailField(max_length=256)
#     name=models.CharField(max_length=256)
#     password=models.CharField(max_length=256)
#     phone=models.CharField(max_length=256)


# class PersonForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         fields="__all__"



# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=20)
    rollno = models.IntegerField(default= 6100)
    
    def __str__(self):
        return self.name
    
