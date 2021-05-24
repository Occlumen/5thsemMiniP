from django.urls import path
from . import views

urlpatterns = [
    path('addevent/', views.addevent, name='Add Event Page'),
    path('back', views.back, name='Task And Event Page'),
    path('adde', views.adde, name='Add Event Page')
]