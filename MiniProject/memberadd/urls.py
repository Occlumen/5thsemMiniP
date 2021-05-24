from django.urls import path
from . import views

urlpatterns = [
    path('memberadd/', views.memberadd, name='Member Add Page'),
    path('logout', views.logout, name='Home Page'),
    path('addbookp', views.addbookp, name='Member Add Page'),
]