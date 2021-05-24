from django.contrib import auth
from django.contrib.auth import login
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.utils import timezone

from homepage.models import VolunteerBasic


def volunteerlogin(request):
    return render(request, 'volunteerloginpage.html')


def volunteeraccount(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Password']
        x = auth.authenticate(username=username, password=password, first_name='V')
        if x is None:
            return render(request, 'volunteerloginpage.html')
        else:
            auth.login(request, x)
            x.save()
            print(username)
            print("Volunteer logged in.")
            return render(request, 'volunteeraccountpage.html')
