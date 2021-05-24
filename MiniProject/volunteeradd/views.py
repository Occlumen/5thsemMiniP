from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from homepage.models import Volunteerdonation, VolunteerBasic
# Create your views here.
def volunteeradd(request):
    return render(request, 'volunteeraddpage.html')


def logout(request):
    return redirect('/')


def adddonation(request):
    if request.method == 'POST':
        dateofdonation = request.POST['dod']
        bookname = request.POST['bookname']
        deptofbook = request.POST['department']
        publishedyear = request.POST['pubyear']
        edition = request.POST['edition']
        condofbook = request.POST['condition']
        y = request.user
        print(y)
        z = VolunteerBasic.objects.get(username=y)
        x = Volunteerdonation(bookname=bookname, deptofbook=deptofbook, edition=edition,
                              publishedyear=publishedyear, condofbook=condofbook, dateofdonation=dateofdonation,
                              usn_id=z.id, user_id=y.id)
        x.save()
        print(bookname)
        print(deptofbook)
        print("Donation Added.")
        return render(request, 'volunteeraddpage.html')
    else:
        return render(request, 'volunteeraddpage.html')
