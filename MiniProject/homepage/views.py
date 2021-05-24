from django.shortcuts import render, redirect

# Create your views here.
from homepage.models import FeedBack


def homepage(request):
    return render(request, 'homepage.html')


def memberlogin(request):
    return render(request, 'memberloginpage.html')


def memberaccount(request):
    return render(request, 'memberaccountpage.html')


def volunteerlogin(request):
    return render(request, 'volunteerloginpage.html')


def volunteeraccount(request):
    return render(request, 'volunteeraccountpage.html')


def membersignup(request):
    return render(request, 'membersignuppage.html')


def volunteersignup(request):
    return render(request, 'volunteersignuppage.html')


def getstarted1(request):
    return render(request, 'getstarted-1page.html')


def getstarted2(request):
    return render(request, 'getstarted-2page.html')


def send(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    subject = request.POST['subject']
    message = request.POST['message']
    x = FeedBack(name=name, email=email, phone=phone, subject=subject, message=message)
    x.save()
    print("Feed Back Recorded.")
    return redirect('/')