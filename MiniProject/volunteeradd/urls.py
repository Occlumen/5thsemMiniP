from django.urls import path
from . import views

urlpatterns = [
    path('volunteeradd/', views.volunteeradd, name='Volunteer Add Page'),
    path('logout', views.logout, name='Home Page'),
    path('adddonation', views.adddonation, name='Volunteer Add Page'),
]