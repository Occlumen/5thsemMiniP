from django.urls import path
from . import views

urlpatterns = [
    path('memberremove', views.memberremove, name='Member Remove Page'),
    path('logout', views.logout, name='Home Page'),
    path('removebookp', views.removebookp, name='Member Remove Page'),
]