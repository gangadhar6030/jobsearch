from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Company(models.Model):
    jobposition = models.CharField(max_length=30)
    level = models.CharField(max_length=30)
    jobdescription = models.TextField()
    requiredskills = models.TextField()
    phonenumber= models.CharField(max_length=10)
    emailaddress = models.EmailField()

class Jobseekers(models.Model):
    education = models.CharField(max_length=30)
    skills = models.TextField()
    projectname = models.TextField()
    projectdescription = models.TextField()
    accomplishments = models.TextField()
    phone= models.CharField(max_length=10)
    email = models.EmailField()