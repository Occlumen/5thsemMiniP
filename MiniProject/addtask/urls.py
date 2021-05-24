from django.urls import path
from . import views

urlpatterns = [
    path('addtask/', views.addtask, name='Add Task Page'),
    path('back', views.back, name='Task And Event Page'),
    path('addt', views.addt, name='Add Task Page')
]