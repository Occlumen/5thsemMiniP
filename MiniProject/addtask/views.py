from django.shortcuts import render
from homepage.models import Volunteertask, VolunteerBasic


# Create your views here.
def addtask(request):
    return render(request, 'addtaskpage.html')


def back(request):
    return render(request, 'taskandeventpage.html')


def addt(request):
    if request.method == 'POST':
        taskname = request.POST['taskname']
        taskdesc = request.POST['taskdesc']
        dateofexecution = request.POST['dateofexe']
        taskloc = request.POST['taskloc']
        y = request.user
        z = VolunteerBasic.objects.get(username=y)
        x = Volunteertask(user_id=y.id, usn_id=z.id, taskname=taskname, taskdesc=taskdesc,
                          dateofexecution=dateofexecution, taskloc=taskloc)
        x.save()
        print(taskname)
        print(taskdesc)
        print("Task Added.")
        return render(request, 'addtaskpage.html')
    else:
        return render(request, 'addtaskpage.html')