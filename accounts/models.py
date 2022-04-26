from django import forms
from django.db import models

# Create your models here.


class Hostel(models.Model):
    Hostel_Name = models.CharField(max_length= 30)
    Location = models.CharField(max_length= 30)
    def __str__(self):
        return self.Hostel_Name


class Student(models.Model):
    Username = models.CharField(max_length=20)
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Regnum = models.CharField(max_length=20)
    Gender = models.CharField(max_length=20)
    Room_no = models.IntegerField(null=True)
    Email = models.CharField(max_length=40)
    Phone_no = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.Regnum
    

