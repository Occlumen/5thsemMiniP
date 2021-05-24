from django.urls import path
from . import views

urlpatterns = [
    path('volunteerdonation', views.volunteerdonation, name='Volunteer Donation Page'),
    path('logout', views.logout, name='Home Page'),
    path('back', views.back, name='Volunteer Account Page'),
    path('vremove', views.vremove, name='Volunteer Remove Page'),
    path('add', views.add, name='Volunteer Add Page')
]