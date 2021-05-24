from django.contrib import admin
from .models import FeedBack, MemberBasic, MemberIssue, VolunteerBasic, Volunteertask, Volunteerevent, Volunteerdonation

# Register your models here.

admin.site.register(FeedBack)
admin.site.register(MemberBasic)
admin.site.register(MemberIssue)
admin.site.register(VolunteerBasic)
admin.site.register(Volunteerdonation)
admin.site.register(Volunteertask)
admin.site.register(Volunteerevent)

