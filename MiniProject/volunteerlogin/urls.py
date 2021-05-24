from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('volunteerlogin/', views.volunteerlogin, name='Volunteer Login Page'),
    path('volunteeraccount', views.volunteeraccount, name='Volunteer Account Page')
]