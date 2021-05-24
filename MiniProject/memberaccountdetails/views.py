from django.shortcuts import render, redirect


# Create your views here.
def memberaccountdetails(request):
    return render(request, 'memberaccountdetailspage.html')


def mlogout(request):
    return redirect('/')


def mback(request):
    return redirect('/getstarted1/memberlogin/')