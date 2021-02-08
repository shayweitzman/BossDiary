from django.shortcuts import render, get_object_or_404,redirect
from workers.models import Job,Worker,Payment
from functools import reduce
import datetime
from django.contrib.admin.views.decorators import staff_member_required




@staff_member_required
def reports1(request):
    return render(request,'reports/reports.html')


@staff_member_required
def jobsperuser(request):
    switch = 1
    workers = Worker.objects.all()
    jobs= Job.objects.all()
    if request.method == "GET":
        return render(request, 'reports/jobsperuser.html', {"switch": switch, "workers": workers[::-1]})
    else:
        switch=0
        res=[]
        res1=()
        worker1=request.POST.get('worker')
        month = request.POST.get('month')
        year = request.POST.get('year')
        worker1=Worker.objects.filter(name=worker1)
        worker1=worker1[0]
        if month=='all':
            if year=='all':
                for job6 in jobs:
                    if worker1 in job6.workers.all() :
                        res1=[job6,2]
                        for job7 in worker1.jobchange.all():
                            if job7.name==job6.name:
                                res1[1]=job7.changehours
                                res.append(res1)
            else:
                for job6 in jobs:
                    if int(job6.date.year) == int(year):
                        if worker1 in job6.workers.all():
                            res1 = [job6, 2]
                            for job7 in worker1.jobchange.all():
                                if job7.name == job6.name:
                                    res1[1] = job7.changehours
                                    res.append(res1)
        else:
            for job6 in jobs:
                if int(job6.date.month) == int(month):
                    if worker1 in job6.workers.all():
                        res1 = [job6, 2]
                        for job7 in worker1.jobchange.all():
                            if job7.name == job6.name:
                                res1[1] = job7.changehours
                                res.append(res1)
        sumhours=0
        for i in res:
            sumhours+=i[1]
        totalamount=20*sumhours
        return render(request, 'reports/jobsperuser.html', {"switch": switch,"worker":worker1,"jobs":res[::-1],"totalamount":totalamount,"month":month,"year":year})


@staff_member_required
def paymentperworker(request):
    switch=1
    payments=Payment.objects.all()
    allworkers=Worker.objects.all()
    if request.method=="GET":
        return render(request, 'reports/paymentperworker.html',{"switch":switch,"workers":allworkers[::-1]})
    else:
        switch=0
        res=[]
        worker1=request.POST.get('worker')
        month = request.POST.get('month')
        year = request.POST.get('year')
        if month=='all':
            if year=='all':
                for payment in payments:
                    workers = payment.workers.filter(name=worker1)
                    if workers:
                        res.append(payment)
            else:
                for payment in payments:
                    workers = payment.workers.filter(name=worker1)
                    if workers:
                        if int(payment.date.year) == int(year):
                            res.append(payment)
        else:
            for payment in payments:
                workers = payment.workers.filter(name=worker1)
                if workers:
                    if int(payment.date.month) == int(month) and int(payment.date.year) == int(year):
                        res.append(payment)
        totalamount = reduce(lambda x,y:x+y,map(lambda x:x.money,res),0)
        return render(request, 'reports/paymentperworker.html', {"switch": switch,"payments":res[::-1],"month":month,"year":year, "totalamount":totalamount,"worker":worker1})


@staff_member_required
def paymentreport(request):
    workers=Worker.objects.all()
    return render(request,'reports/paymentsreport.html',{"workers":workers[::-1]})


@staff_member_required
def jobspermonth(request):
    switch=1
    jobs=Job.objects.all()
    today = datetime.date.today()
    currmonth=today.month
    curryear=today.year
    if request.method=="GET":
        return render(request, 'reports/jobspermonth.html',{"switch":switch,"todaymonth":currmonth,"todayyear":curryear})
    else:
        switch=0
        res=[]
        month = request.POST.get('month')
        year = request.POST.get('year')
        for job in jobs:
            if int(job.date.month) == int(month) and int(job.date.year) == int(year):
                res.append(job)

        return render(request, 'reports/jobspermonth.html', {"switch": switch,"jobs":res[::-1],"month":month,"year":year})

@staff_member_required
def paymentspermonth(request):
    switch=1
    payments=Payment.objects.all()
    today = datetime.date.today()
    currmonth = today.month
    curryear = today.year
    if request.method=="GET":
        return render(request, 'reports/paymentspermonth.html',{"switch":switch,"todaymonth":currmonth,"todayyear":curryear})
    else:
        switch=0
        res=[]

        month = request.POST.get('month')
        year = request.POST.get('year')
        for payment in payments:
            if int(payment.date.month) == int(month) and int(payment.date.year) == int(year):
                res.append(payment)
        return render(request, 'reports/paymentspermonth.html', {"switch": switch,"payments":res[::-1],"month":month,"year":year})

