from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from homepage.models import VolunteerBasic


def volunteersignup(request):
    return render(request, 'volunteersignuppage.html')


def volunteerlogin(request):
    if request.method == 'POST':
        usn = request.POST['USN']
        firstname = request.POST['first-name']
        lastname = request.POST['lastname']
        dob = request.POST['dob']
        department = request.POST['department']
        email = request.POST['email']
        contactnumber = request.POST['contact-number']
        username = request.POST['username']
        password = request.POST['Password']
        z = auth.authenticate(username = username)
        if z is not None:
            messages.warning(request , 'Username already exists  !!!!!!!')
        else:
            x = VolunteerBasic(usn=usn, firstname=firstname, lastname=lastname, dob=dob, department=department,
                           email=email, contactnumber=contactnumber, username=username, password=password)
            y = User.objects.create_user(username=username, password=password, first_name='V')
            y.save()
            x.save()
            print(firstname)
            print(username)
            print("Volunteer Added.")
            return redirect('/getstarted1/volunteerlogin/')
    else:
        return render(request, 'volunteersignuppage.html')
