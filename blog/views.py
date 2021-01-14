from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Company
from blog.models import Jobseekers

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')
def company(request):
    if request.method=="POST":
        jobposition=request.POST['jobposition']
        level=request.POST['level']
        jobdescription=request.POST['jobdescription']
        requiredskills=request.POST['requiredskills']
        phonenumber=request.POST['phonenumber']
        emailaddress=request.POST['emailaddress']
        ins = Company(jobposition=jobposition, level=level, jobdescription=jobdescription, requiredskills=requiredskills, phonenumber=phonenumber, emailaddress=emailaddress)
        ins.save()
        print("the data has been written in the DB")
    return render(request, 'blog/company.html')
   
def jobseekers(request):
    if request.method=="POST":
        education=request.POST['education']
        skills=request.POST['skills']
        projectname=request.POST['projectname']
        projectdescription=request.POST['projectdescription']
        accomplishments=request.POST['accomplishments']
        phone=request.POST['phone']
        email=request.POST['email']
        inp = Jobseekers(education=education, skills=skills, projectname=projectname, projectdescription=projectdescription, accomplishments=accomplishments, phone=phone, email=email)
        inp.save()
        print("the data has been written in the DB")
    return render(request, 'blog/jobseekers.html')

def searchingpage(request):
    com = Company.objects.all()
    print(com)
    context = {'comp': com}
    return render(request, 'blog/searchingpage.html', context)

