from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('getstarted1/', views.getstarted1, name='Get Started Page 1'),
    path('getstarted2/', views.getstarted2, name='Get Started Page 1'),
    path('memberlogin/', views.memberlogin, name='Member Login Page'),
    path('volunteerlogin/', views.volunteerlogin, name='Volunteer Login Page')
]