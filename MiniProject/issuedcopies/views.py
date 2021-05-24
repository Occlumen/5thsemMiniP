from django.shortcuts import render, redirect

# Create your views here.
from homepage.models import MemberIssue

def issuedcopies(request):
    return render(request, 'issuedcopiespage.html')

def logout(request):
    return redirect('/')

