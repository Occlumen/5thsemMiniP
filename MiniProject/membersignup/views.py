from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from homepage.models import MemberBasic


def membersignup(request):
    return render(request, 'membersignuppage.html')


def memberlogin(request):
    if request.method == 'POST':
        usn = request.POST['usn']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        dob = request.POST['dateofbirth']
        department = request.POST['department']
        email = request.POST['email']
        contactnumber = request.POST['contactnumber']
        username = request.POST['username']
        password = request.POST['password']
        x = MemberBasic(usn=usn, firstname=firstname, lastname=lastname, dob=dob, department=department,
                           email=email, contactnumber=contactnumber, username=username, password=password)
        y = User.objects.create_user(username=username, password=password, first_name='M')
        y.save()
        x.save()
        print(firstname)
        print(username)
        print("Member Added.")
        return render(request, 'memberloginpage.html')
    else:
        return render(request, 'membersignuppage.html')

