from django.db import models
from django.forms import BooleanField

# Create your models here.

class homemenu(models.Model):

    name = models.CharField(max_length=100)
    img= models.ImageField(upload_to ='pics') 
    des = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


messtime_choices = (
    ('Lunch', 'lunch'),
    ('Dinner', 'dinner')
)

class Menu(models.Model):
    name = models.CharField(max_length=100)
    day = models.CharField(max_length=30)
    desc = models.TextField(null=True)
    Price = models.IntegerField(null=True)
    time = models.CharField(max_length=8, choices=messtime_choices, blank=True)
    def __str__(self):
        return self.name
    

