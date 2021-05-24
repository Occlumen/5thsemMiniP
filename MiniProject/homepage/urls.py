from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='Home Page'),
    path('memberlogin/', views.memberlogin, name='Member Login Page'),
    path('memberaccount/', views.memberaccount, name='Member Account Page'),
    path('volunteerlogin/', views.volunteerlogin, name='Volunteer Login Page'),
    path('volunteeraccount/', views.volunteeraccount, name='Volunteer Account Page'),
    path('membersignup/', views.membersignup, name='Member Sign Up Page'),
    path('volunteersignup/', views.volunteersignup, name='Volunteer Sign Up Page'),
    path('getstarted1/', views.getstarted1, name='Get Started Page 1'),
    path('getstarted2/', views.getstarted2, name='Get Started Page 1'),
    path('send', views.send, name='Send Button')
]