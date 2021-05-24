from django.urls import path
from . import views

urlpatterns = [
    path('removetask', views.removetask, name='Remove Task Page'),
    path('back', views.back, name='Task And Event Page'),
    path('removet', views.removet, name='Remove Task Page')
]