from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class FeedBack(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=35)
    phone = models.BigIntegerField()
    subject = models.CharField(max_length=20)
    message = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class MemberBasic(models.Model):
    usn = models.CharField(max_length=10)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    dob = models.DateField()
    department = models.CharField(max_length=20)
    email = models.EmailField(max_length=35)
    contactnumber = models.BigIntegerField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.usn


class VolunteerBasic(models.Model):
    usn = models.CharField(max_length=10)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    dob = models.DateField()
    department = models.CharField(max_length=20)
    email = models.EmailField(max_length=35)
    contactnumber = models.BigIntegerField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.usn


class MemberIssue(models.Model):
    usn = models.ForeignKey(MemberBasic, default='None', on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    bookname = models.CharField(max_length=30)
    deptofbook = models.CharField(max_length=30)
    edition = models.CharField(max_length=10)
    publishedyear = models.CharField(max_length=10)
    condofbook = models.CharField(max_length=30)
    dateofissue = models.DateField()



class Volunteerdonation(models.Model):
    usn = models.ForeignKey(VolunteerBasic, default='None', on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    bookname = models.CharField(max_length=30)
    deptofbook = models.CharField(max_length=30)
    edition = models.CharField(max_length=10)
    publishedyear = models.CharField(max_length=10)
    condofbook = models.CharField(max_length=30)
    dateofdonation = models.DateField()



class Volunteertask(models.Model):
    usn = models.ForeignKey(VolunteerBasic, default='None', on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    taskname = models.CharField(max_length=30)
    taskdesc = models.CharField(max_length=50)
    dateofexecution = models.DateField()
    taskloc = models.CharField(max_length=30)


class Volunteerevent(models.Model):
    usn = models.ForeignKey(VolunteerBasic, default='None', on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    eventname = models.CharField(max_length=30)
    eventdesc = models.CharField(max_length=50)
    dateofexecution = models.DateField()
    eventloc = models.CharField(max_length=30)
