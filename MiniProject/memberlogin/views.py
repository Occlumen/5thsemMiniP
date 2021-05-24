from django.contrib import auth
from django.contrib.auth import login
from django.shortcuts import render

# Create your views here.
from django.utils import timezone

from homepage.models import MemberBasic


def memberlogin(request):
    return render(request, 'memberloginpage.html')


def memberaccount(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        y = auth.authenticate(username=username, password=password, first_name='M')
        if y is None:
            return render(request, 'memberloginpage.html')
        else:
            auth.login(request, y)
            y.save()
            print(username)
            print("Member logged in.")
            return render(request, 'memberaccountpage.html')
