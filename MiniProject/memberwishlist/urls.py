from django.urls import path
from . import views

urlpatterns = [
    path('memberwishlist/', views.memberwishlist, name='Member Wishlist Page'),
    path('logout', views.logout, name='Home Page'),
    path('back', views.back, name='Volunteer Account Page'),
    path('addbook', views.addbook, name='Member Add Page'),
    path('removebook', views.removebook, name='Member Remove Page')
]