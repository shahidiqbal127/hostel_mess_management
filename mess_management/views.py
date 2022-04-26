from django.shortcuts import render
from .models import *
# Create your views here.




def index(request):

    dests = homemenu.objects.all()    
    return render(request, 'index.html', {'dests': dests}) 

def menu(request):
    Lmenu = Menu.objects.filter(time='Lunch')
    Dmenu = Menu.objects.filter(time='Dinner')
    return render(request,'menu.html',context={'Lmenu':Lmenu,'Dmenu':Dmenu})

def about(request):
    
    return render(request, 'about.html') 
