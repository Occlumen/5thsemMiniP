# Generated by Django 3.1.4 on 2021-01-15 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=35)),
                ('phone', models.BigIntegerField()),
                ('subject', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MemberBasic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usn', models.CharField(max_length=10)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('department', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=35)),
                ('contactnumber', models.BigIntegerField()),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerBasic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usn', models.CharField(max_length=10)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('department', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=35)),
                ('contactnumber', models.BigIntegerField()),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteertask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=30)),
                ('taskdesc', models.CharField(max_length=50)),
                ('dateofexecution', models.DateField()),
                ('taskloc', models.CharField(max_length=30)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('usn', models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='homepage.volunteerbasic')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteerevent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=30)),
                ('eventdesc', models.CharField(max_length=50)),
                ('dateofexecution', models.DateField()),
                ('eventloc', models.CharField(max_length=30)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('usn', models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='homepage.volunteerbasic')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteerdonation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=30)),
                ('deptofbook', models.CharField(max_length=30)),
                ('edition', models.CharField(max_length=10)),
                ('publishedyear', models.CharField(max_length=10)),
                ('condofbook', models.CharField(max_length=30)),
                ('dateofdonation', models.DateField()),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('usn', models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='homepage.volunteerbasic')),
            ],
        ),
        migrations.CreateModel(
            name='MemberIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=30)),
                ('deptofbook', models.CharField(max_length=30)),
                ('edition', models.CharField(max_length=10)),
                ('publishedyear', models.CharField(max_length=10)),
                ('condofbook', models.CharField(max_length=30)),
                ('dateofissue', models.DateField()),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('usn', models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='homepage.memberbasic')),
            ],
        ),
    ]
