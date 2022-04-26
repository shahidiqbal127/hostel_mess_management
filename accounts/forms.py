from django import forms
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student


class StudentSignUpForm(forms.ModelForm):
    
    Password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    

    class Meta:
        model = Student
        fields = [
            'Username',
            'First_name',
            'Last_name',
            'Password',
            'Regnum',
            'Email',
            'Gender',
            'Room_no',
            'Phone_no',
            'hostel']


class LoginForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'Username',
            'Password']
