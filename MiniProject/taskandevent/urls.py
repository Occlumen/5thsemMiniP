from django.urls import path
from . import views

urlpatterns = [
    path('taskandevent', views.taskandevent, name='Task And Event Page'),
    path('back', views.back, name='Volunteer Account Page'),
    path('addtask', views.addtask, name='Add Task Page'),
    path('removeevent', views.removeevent, name='Remove Event Page'),
    path('addevent', views.addevent, name='Add Task Page'),
    path('removetask', views.removetask, name='Remove Event Page')
]