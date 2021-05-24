from django.urls import path
from . import views

urlpatterns = [
    path('removeevent', views.removeevent, name='Remove Event Page'),
    path('back', views.back, name='Task And Event Page'),
    path('remove', views.remove, name='Remove Event Page')
]