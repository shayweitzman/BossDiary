from django.shortcuts import render, get_object_or_404,redirect
from workers.models import Worker, Job as job
from workers.forms import JobForm



def homepage(request):
    return render(request,'homepage/homepage.html')


