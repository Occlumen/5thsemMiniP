from django.urls import path
from . import views

urlpatterns = [
    path('volunteerremove', views.volunteerremove, name='Remove Event Page'),
    path('back', views.back, name='Task And Event Page'),
    path('volunteerremove', views.volunteerremove, name='Remove Event Page')
]