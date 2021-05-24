from django.shortcuts import render, redirect


# Create your views here.

def getstarted1(request):
    return redirect('/getstarted1/')


def getstarted2(request):
    return render(request, 'getstarted-2page.html')


def membersignup(request):
    return render(request, 'membersignuppage.html')


def volunteersignup(request):
    return render(request, 'volunteersignuppage.html')