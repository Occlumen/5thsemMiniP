from django.contrib import auth
from django.shortcuts import render, redirect

# Create your views here.
from homepage.models import Volunteerdonation, MemberIssue, MemberBasic


def memberaccount(request):
    return render(request, 'memberaccountpage.html')

def logout(request):
    return redirect('/')


def memberwishlist(request):
    y = request.user
    print(y)
    wishlist = Volunteerdonation.objects.all()
    return render(request, 'memberwishlistpage.html', {'wishlist': wishlist})

def issuedcopies(request):
    y = request.user
    z = MemberBasic.objects.get(username=y)
    issues = MemberIssue.objects.filter(usn_id=z.id)
    return render(request, 'issuedcopiespage.html', {'issues': issues})

def memberaccountdetails(request):
    return render(request, 'memberaccountdetailspage.html')
