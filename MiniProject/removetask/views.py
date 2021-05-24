from django.shortcuts import render

# Create your views here.
from homepage.models import Volunteerevent, Volunteertask


def removetask(request):
    return render(request, 'removetaskpage.html')


def back(request):
    return render(request, 'taskandeventpage.html')


def removet(request):
    if request.method == 'POST':
        task = request.POST['task']
        print(task)
        y = Volunteertask.objects.get(id=task)
        print(y.taskname)
        x = Volunteertask.objects.get(id=task).delete()
        print("Task Removed .")
        return render(request, 'removetaskpage.html')
    else:
        return render(request, 'removetaskpage.html')

