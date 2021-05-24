from django.shortcuts import render
from homepage.models import Volunteerevent

# Create your views here.
def removeevent(request):
    return render(request, 'removeeventpage.html')


def back(request):
    return render(request, 'taskandeventpage.html')


def remove(request):
    if request.method == 'POST':
        event = request.POST['event']
        print(event)
        y = Volunteerevent.objects.get(id=event)
        print(y.eventname)
        x = Volunteerevent.objects.get(id=event).delete()
        print("Event Removed .")
        return render(request, 'removeeventpage.html')
    else:
        return render(request, 'removeeventpage.html')

