from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('membersignup/', views.membersignup, name='Member Sign Up Page'),
    path('volunteersignup/', views.volunteersignup, name='Volunteer Sign Up Page'),
    path('getstarted1/', views.getstarted1, name='Get Started Page 1'),
    path('getstarted2/', views.getstarted2, name='Get Started Page 1')
]