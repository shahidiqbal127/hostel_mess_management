from distutils.command.upload import upload
from pickle import FALSE
from django.db import models
from django.forms import BooleanField

# Create your models here.

class Destination(models.Model):

    name = models.CharField(max_length=100)
    img= models.ImageField(upload_to ='pics') 
    des = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=FALSE)


