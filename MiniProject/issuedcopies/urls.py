from django.urls import path
from . import views

urlpatterns = [
    path('issuedcopies', views.issuedcopies, name='Issued Copies Page'),
    path('logout', views.logout, name='Home Page')
]