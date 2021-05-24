from django.shortcuts import render

# Create your views here.
from homepage.models import VolunteerBasic, Volunteerevent, Volunteertask


def taskandevent(request):
    return render(request, 'taskandeventpage.html')


def back(request):
    return render(request, 'volunteeraccountpage.html')


def addtask(request):
    return render(request, 'addtaskpage.html')


def addevent(request):
    return render(request, 'addeventpage.html')

def removetask(request):
    y = request.user
    z = VolunteerBasic.objects.get(username=y)
    tasks = Volunteertask.objects.filter(usn_id=z.id)
    return render(request, 'removetaskpage.html', {'tasks': tasks})

def removeevent(request):
    y = request.user
    z = VolunteerBasic.objects.get(username=y)
    events = Volunteerevent.objects.filter(usn_id=z.id)
    return render(request, 'removeeventpage.html', {'events': events})