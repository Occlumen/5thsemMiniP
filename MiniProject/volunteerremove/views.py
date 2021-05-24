from django.shortcuts import render, redirect

from homepage.models import Volunteerevent, Volunteerdonation


# Create your views here.
def volunteerremove(request):
    return render(request, 'volunteerremovepage.html')


def back(request):
    return redirect('/getstarted1/volunteerlogin/')


def volunteerremove(request):
    if request.method == 'POST':
        donation = request.POST['donation']
        print(donation)
        y = Volunteerdonation.objects.get(id=donation)
        print(y.bookname)
        x = Volunteerdonation.objects.get(id=donation).delete()
        print("Donation Removed .")
        return render(request, 'volunteerremovepage.html')
    else:
        return render(request, 'removeeventpage.html')

