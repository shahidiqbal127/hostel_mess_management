from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, StudentSignUpForm
from .models import Student

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')



def student_register(request):
    form = StudentSignUpForm()
    if request.method == 'POST':
       form = StudentSignUpForm(request.POST)    
       if form.is_valid():
           form.save()
           Username = form.cleaned_data.get('Username')
           Password = form.cleaned_data.get('Password')
           user=User.objects.create_user(username=Username,password=Password)
           user.save()
           messages.success(request,f'Account Created for ' + Username)
           return redirect('login_request')
    else:
        form = StudentSignUpForm()
    return render(request, 'student_register.html', {'form': form})

def login_request(request):
    #form = LoginForm(request.POST)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #if form.is_valid():
            #Username = form.cleaned_data.get('Username')
            #Password = form.cleaned_data.get('Password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/')
    else:
        
        #messages.info(request, 'Form was invalid')
        return render(request, 'login.html')
                       
        
    #else:
     #   messages.info(request,'Validation Error')   
      #  return render(request, 'login.html')


def menu(request):
    if request.method == 'POST':
       form = StudentSignUpForm(request.POST)    
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(request,f'Account Created')
           print('USER Created');
           return redirect('login')
    else:
        form = StudentSignUpForm()
    return render(request, 'menu.html', {'form': form})


