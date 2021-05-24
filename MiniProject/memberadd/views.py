from django.shortcuts import render, redirect

# Create your views here.
from homepage.models import Volunteerdonation, MemberIssue, MemberBasic


def memberadd(request):
    return render(request, 'memberaddpage.html')


def logout(request):
    return redirect('/')


def addbookp(request):
    book = request.POST['book']
    print(book)
    z = request.user
    print(z)
    k = MemberBasic.objects.get(username=z.username)
    y = Volunteerdonation.objects.get(id=book)
    x = MemberIssue(bookname=y.bookname, deptofbook=y.deptofbook, edition=y.edition, publishedyear=y.publishedyear,
                    condofbook=y.condofbook, dateofissue=y.dateofdonation, user_id=z.id, usn_id=k.id)
    x.save()
    print(y.bookname)
    print(y.deptofbook)
    print("Member Issue Updated")
    donations = Volunteerdonation.objects.all()
    return render(request, 'memberaddpage.html', {'donations': donations})



