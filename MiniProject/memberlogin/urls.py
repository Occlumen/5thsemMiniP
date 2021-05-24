from django.urls import path
from . import views

urlpatterns = [
    path('memberlogin/', views.memberlogin, name='Member Login Page'),
    path('memberaccount', views.memberaccount, name='Member Account Page')
]