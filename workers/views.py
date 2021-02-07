from django.shortcuts import render, get_object_or_404,redirect
from workers.models import Worker as worker ,Payment as paymentmodel ,Job as job
from workers.forms import JobForm,ReduceHrs,Payment,WorkerForm,AddHrsAndWorkers
import datetime
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def addhrsandworkers(request):
    jobs = job.objects.all()
    if request.method == "GET":
        return render(request, 'addhrsandworkers/addhrsandworkers.html', {'jobs': jobs[::-1], "form": AddHrsAndWorkers()})
    elif request.method == "POST":
        form = AddHrsAndWorkers(request.POST)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.save()
            form.save_m2m()
            job1 = request.POST.get('job')
            selectedjob = job.objects.filter(id=job1)
            updatehrs3(newForm)
            totaladdhrs = newForm.total_hours * len(newForm.workers.all())
            for jobb in selectedjob:
                jobb.all_hours += totaladdhrs
                jobb.total_amount += (totaladdhrs * newForm.Money_For_Hour)
                jobb.money += newForm.money
                jobb.left = jobb.total_amount - jobb.money
                for wrkr in newForm.workers.all():
                    if wrkr not in jobb.workers.all():
                        jobb.workers.add(wrkr)
                jobb.save()
            newForm.delete()
            return render(request, 'addhrsandworkers/addhrsandworkers.html',
                          {'jobs': jobs[::-1], "form": AddHrsAndWorkers()})

        else:
            return render(request, 'addhrsandworkers/addhrsandworkers.html', {'jobs': jobs[::-1], "form": AddHrsAndWorkers(), "error": "Not Good"})


def updatehrs3(form_ins):
    jobs = job.objects.filter(name=form_ins.name)
    for worker1 in jobs[0].workers.all():
        worker1.total_hours += form_ins.total_hours
        worker1.total_money += form_ins.total_hours * 20
        worker1.own += form_ins.total_hours * 20
        worker1.save()






@staff_member_required
def ReduceHrs1(request):
    flag=0
    jobs = job.objects.all()
    if request.method == "GET":
        return render(request, 'reducehrs/reducehrs.html', {'jobs': jobs[::-1], "form": ReduceHrs()})
    elif request.method == "POST":
        form = ReduceHrs(request.POST)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.save()
            form.save_m2m()
            job1 = request.POST.get('job')
            selectedjob = job.objects.filter(id=job1)
            for worker5 in newForm.workers.all():
                if worker5 not in selectedjob[0].workers.all():
                    flag=1
            if newForm.total_hours<=selectedjob[0].all_hours and len(newForm.workers.all())!=0 and flag==0:
                error=""
                updatehrs(newForm)
                totalreducehrs = newForm.total_hours * len(newForm.workers.all())
                for jobb in selectedjob:
                    jobb.all_hours -= totalreducehrs
                    jobb.total_amount -= (totalreducehrs * selectedjob[0].Money_For_Hour)
                    jobb.left = jobb.total_amount - jobb.money
                    jobb.save()
            else:
                if len(newForm.workers.all())==0:
                    error="לא נבחר עובד"
                elif flag:
                    error = "העובד שנבחר לא קיים בעבודה זו"
                else:
                    error="אין מספיק שעות להוריד"
            newForm.delete()
            return render(request, 'reducehrs/reducehrs.html',
                          {'jobs': jobs[::-1], "form": ReduceHrs(), "error": error})

        else:
            return render(request, 'reducehrs/reducehrs.html', {'jobs': jobs[::-1], "form": ReduceHrs(), "error": "Not Good"})


def updatehrs(form_ins):
    jobs = job.objects.filter(name=form_ins.name)
    for worker1 in jobs[0].workers.all():
        if worker1.total_hours-form_ins.total_hours>=0:
            worker1.total_hours -= form_ins.total_hours
            worker1.total_money -= form_ins.total_hours * 20
            worker1.own -= form_ins.total_hours * 20
            worker1.save()

@staff_member_required
def AddWorker(request):
    workers = worker.objects.all()
    if request.method == "GET":
        return render(request, 'addworker/addworker.html',{'workers':workers,"form":WorkerForm()})
    elif request.method == "POST":
        form = WorkerForm(request.POST)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.save()
            # form.save_m2m()
            # updateall(newForm)
            return redirect("addworker")
        else:
            return render(request, 'addworker/addworker.html', {'workers': workers, "form": WorkerForm(),"error":"קיים כבר עובד עם שם זה"})



@staff_member_required
def Job(request):
    jobs = job.objects.all()
    if request.method == "GET":
        return render(request, 'addwork/addwork.html',{'jobs':jobs,"form":JobForm()})
    elif request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.save()
            form.save_m2m()
            updateall(newForm)
            newForm.all_hours=len(newForm.workers.all()) * newForm.total_hours
            newForm.total_amount = newForm.all_hours* newForm.Money_For_Hour
            newForm.left = newForm.total_amount - newForm.money

            newForm.save()

            return redirect("addjob")
        else:
            return render(request, 'addwork/addwork.html', {'jobs': jobs, "form": JobForm(),"error":"Not Good"})


def updateall(form_ins):
    jobs= job.objects.filter(name=form_ins.name)
    for worker1 in jobs[0].workers.all():
        worker1.total_hours += form_ins.total_hours
        worker1.total_money += form_ins.total_hours*20
        worker1.own += form_ins.total_hours * 20
        worker1.save()

@staff_member_required
def updatepaymentforjob(request):
    switch = 1
    jobs= job.objects.all()
    if request.method == "GET":
        return render(request, 'updatepayment/updatepaymentforjob.html',{"switch": switch,"jobs":jobs[::-1]})
    else:
        switch = 1
        res = []
        job1 = request.POST.get('job')
        amount= request.POST.get('amount')
        for job2 in jobs:
            if job2.id == int(job1):
                job2.money+=int(amount)
                job2.left=job2.total_amount-job2.money
                job2.save()
        return render(request, 'updatepayment/updatepaymentforjob.html',{"jobs":jobs[::-1],"switch": switch,"msg":"בוצע בהצלחה"})



@staff_member_required
def Payment1(request):
    jobs = job.objects.all()
    if request.method == "GET":
        return render(request, 'payment/payment.html', {'jobs': jobs, "form": Payment()})
    elif request.method == "POST":
        form = Payment(request.POST)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.save()
            form.save_m2m()
            updatepayment(newForm)
            newForm.delete()
            return redirect("payment")
        else:
            return render(request, 'payment/payment.html', {'jobs': jobs, "form": Payment(), "error": "Not Good"})


def updatepayment(form_ins):
    jobs = job.objects.filter(name=form_ins.name)
    payment = paymentmodel(name=form_ins.name,money=form_ins.money)
    payment.save()
    for worker1 in jobs[0].workers.all():
        worker1.paid += form_ins.money
        worker1.own = worker1.total_money-worker1.paid
        worker1.date=datetime.datetime.now()
        worker1.save()
        payment.workers.add(worker1)
        payment.save()

