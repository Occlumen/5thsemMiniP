from django.urls import path
from . import views

urlpatterns = [
    path('memberaccountdetails', views.memberaccountdetails, name='Member Account Details Page'),
    path('mlogout', views.mlogout, name='Home Page'),
    path('mback', views.mback, name='Member Account Page'),
]