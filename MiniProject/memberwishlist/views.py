from django.shortcuts import render, redirect

# Create your views here.
from homepage.models import Volunteerdonation, MemberIssue


def memberwishlist(request):
    return render(request, 'memberwishlistpage.html')


def logout(request):
    return redirect('/')

def back(request):
    return redirect('/getstarted1/memberlogin/')


def addbook(request):
    donations = Volunteerdonation.objects.all()
    return render(request, 'memberaddpage.html', {'donations': donations})


def removebook(request):
    y = request.user
    print(y)
    z = y.id
    removes = MemberIssue.objects.filter(user_id = z)
    return render(request, 'memberremovepage.html', {'removes': removes})


