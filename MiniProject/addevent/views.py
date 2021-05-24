from django.shortcuts import render
from homepage.models import Volunteertask, VolunteerBasic, Volunteerevent


# Create your views here.
def addevent(request):
    return render(request, 'addeventpage.html')


def back(request):
    return render(request, 'taskandeventpage.html')


def adde(request):
    if request.method == 'POST':
        eventname = request.POST['eventname']
        eventdesc = request.POST['eventdesc']
        dateofexecution = request.POST['dateofexe']
        eventloc = request.POST['eventloc']
        y = request.user
        z = VolunteerBasic.objects.get(username=y)
        x = Volunteerevent(user_id=y.id, usn_id=z.id, eventname=eventname, eventdesc=eventdesc,
                          dateofexecution=dateofexecution, eventloc=eventloc)
        x.save()
        print(eventname)
        print(eventdesc)
        print("Event Added.")
        return render(request, 'addeventpage.html')
    else:
        return render(request, 'addeventpage.html')
