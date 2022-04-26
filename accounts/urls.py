from django.urls import path

from . import views

urlpatterns = [
    path('student_register/', views.student_register, name='student_register'),
    path('login_request/', views.login_request, name='login_request'),
    path('logout/', views.logout, name='logout')
]