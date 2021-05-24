from django.urls import path
from . import views

urlpatterns = [
    path('volunteeraccount', views.volunteeraccount, name='Volunteer Account Page'),
    path('volunteerlogout', views.volunteerlogout, name='Home Page'),
    path('volunteerdonation/', views.volunteerdonation, name='Volunteer Donation Page'),
    path('taskandevent', views.taskandevent, name='Task And Event Page')
]