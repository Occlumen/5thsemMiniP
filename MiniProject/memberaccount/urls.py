from django.urls import path
from . import views

urlpatterns = [
    path('memberaccount', views.memberaccount, name='Member Account Page'),
    path('logout', views.logout, name='Home Page'),
    path('memberwishlist/', views.memberwishlist, name='Member Wishlist Page'),
    path('issuedcopies/', views.issuedcopies, name='Issued Copies Page'),
    path('memberaccountdetails/', views.memberaccountdetails, name='Member Account Details Page')
]