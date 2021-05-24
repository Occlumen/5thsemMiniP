from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('volunteersignup/', views.volunteersignup, name='Volunteer Sign Up Page'),
    path('volunteerlogin', views.volunteerlogin, name='Volunteer Login Page')
]