from django.shortcuts import render, get_object_or_404,redirect
from workers.models import Job,Worker
import datetime




def reports1(request):
    return render(request,'reports/reports.html')

def jobspermonth(request):
    switch=1
    jobs=Job.objects.all()
    if request.method=="GET":
        return render(request, 'reports/jobspermonth.html',{"switch":switch})
    else:
        switch=0
        res=[]
        month = request.POST.get('month')
        year = request.POST.get('year')
        for job in jobs:
            if int(job.date.month) == int(month) and int(job.date.year) == int(year):
                res.append(job)
        res=list(set(res))
        return render(request, 'reports/jobspermonth.html', {"switch": switch,"jobs":res[::-1],"month":month,"year":year})

