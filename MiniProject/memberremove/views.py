
from django.shortcuts import render, redirect
from homepage.models import MemberIssue

# Create your views here.


def memberremove(request):
    y = request.user
    print(y)
    z = y.id
    removes = MemberIssue.objects.filter(user_id=z)
    return render(request, 'memberremovepage.html', {'removes': removes})


def logout(request):
    return redirect('/')


def removebookp(request):
    if request.method == 'POST':
        remove = request.POST['book']
        print(remove)
        y = MemberIssue.objects.get(id=remove)
        print(y.bookname)
        x = MemberIssue.objects.get(id=remove).delete()
        print("Item in wishlist Removed .")
        return render(request, 'memberremovepage.html')
    else:
        return render(request, 'memberremovepage.html')
