from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('membersignup/', views.membersignup, name='Member Sign Up Page'),
    path('memberlogin', views.memberlogin, name='Member Login Page')
]