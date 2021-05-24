from django.shortcuts import render

# Create your views here.

def getstarted1(request):
    return render(request, 'getstarted-1page.html')


def getstarted2(request):
    return render(request, 'getstarted-2page.html')


def memberlogin(request):
    return render(request, 'memberloginpage.html')


def volunteerlogin(request):
    return render(request, 'volunteerloginpage.html')

