from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    dob=models.DateField()
    city=models.CharField(max_length=50)
