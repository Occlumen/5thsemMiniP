from django.shortcuts import render, redirect


# Create your views here.
from homepage.models import Volunteerdonation


def volunteerdonation(request):
    return render(request, 'volunteerdonationpage.html')


def logout(request):
    return redirect('/')


def add(request):
    return render(request, 'volunteeraddpage.html')

def vremove(request):
    y = request.user
    print(y)
    z = y.id
    donations = Volunteerdonation.objects.filter(user_id = z)
    return render(request, 'volunteerremovepage.html', {'donations': donations})

def back(request):
    return redirect('/getstarted1/volunteerlogin/')


def volunteerremove(request):
    return render(request, 'volunteerremovepage.html')