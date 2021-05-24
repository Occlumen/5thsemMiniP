from django.contrib.auth import logout
from django.shortcuts import render, redirect

# Create your views here.
from homepage.models import Volunteerdonation, Volunteertask, Volunteerevent

def volunteeraccount(request):
    return render(request, 'volunteeraccountpage.html')

def volunteerlogout(request):
    return redirect('/')


def volunteerdonation(request):
    y = request.user
    print(y)
    donations = Volunteerdonation.objects.all()
    return render(request, 'volunteerdonationpage.html', {'donations': donations})


def taskandevent(request):
    tasks = Volunteertask.objects.all()
    events = Volunteerevent.objects.all()
    return render(request, 'taskandeventpage.html', {'tasks': tasks, 'events': events})
