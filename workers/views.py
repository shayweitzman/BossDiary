from django.shortcuts import render, get_object_or_404,redirect
from workers.models import Worker as worker ,Payment as paymentmodel ,Job as job,ChangeJob
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
            updatehrs3(newForm,selectedjob[0])
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


def updatehrs3(form_ins,selectedjob):
    jobs = job.objects.filter(name=form_ins.name)
    for worker1 in jobs[0].workers.all():
        for job2 in worker1.jobchange.all():
            if job2.name == selectedjob.name:
                job2.changehours += form_ins.total_hours
                job2.save()
        if selectedjob.name not in list(map(lambda x:x.name,worker1.jobchange.all())):
            new = ChangeJob()
            new.name = selectedjob.name
            new.changehours = form_ins.total_hours
            new.save()
            worker1.jobchange.add(new)
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
            minhour=selectedjob[0].total_hours
            for worker5 in newForm.workers.all():
                if worker5 not in selectedjob[0].workers.all():
                    flag=1
                for job5 in worker5.jobchange.all():
                    if job5.name ==selectedjob[0].name:
                        minhour=min(minhour,job5.changehours)
            if newForm.total_hours<=selectedjob[0].total_hours and len(newForm.workers.all())!=0 and flag==0 and newForm.total_hours<=minhour:
                error=""
                updatehrs(newForm,selectedjob[0])
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


def updatehrs(form_ins,selected):
    jobs = job.objects.filter(name=form_ins.name)
    for worker1 in jobs[0].workers.all():
        if worker1.total_hours-form_ins.total_hours>=0:
            if selected.name not in list(map(lambda x: x.name,worker1.jobchange.all())):
                new=ChangeJob()
                new.name=selected.name
                new.changehours=selected.total_hours-form_ins.total_hours
                new.save()
                worker1.jobchange.add(new)
            else:
                for work in worker1.jobchange.all():
                    if work.name==selected.name:
                        work.changehours-=form_ins.total_hours
                        work.save()
            worker1.total_hours -= form_ins.total_hours
            worker1.total_money -= form_ins.total_hours * 20
            worker1.own -= form_ins.total_hours * 20
            worker1.save()
            #new.delete()

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
    error=""
    if request.method == "GET":
        return render(request, 'addwork/addwork.html',{'jobs':jobs,"form":JobForm()})
    elif request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            newForm = form.save(commit=False)
            if newForm.name in list(map(lambda x:x.name,jobs)):
                print(list(map(lambda x:x.name,jobs)))
                error="קיימת כבר עבודה עם שם זה "
                return render(request, 'addwork/addwork.html', {'jobs': jobs, "form": JobForm(), "error": error})
            else:
                newForm.save()
                form.save_m2m()
                if len(newForm.workers.all())>0:
                    updateall(newForm)
                    newForm.all_hours=len(newForm.workers.all()) * newForm.total_hours
                    newForm.total_amount = newForm.all_hours* newForm.Money_For_Hour
                    newForm.left = newForm.total_amount - newForm.money
                    newForm.save()
                    return render(request, 'addwork/addwork.html', {'jobs': jobs, "form": JobForm(), "error": error})
                else:
                    error="לא נבחרו עובדים"
                    newForm.delete()
                    return render(request, 'addwork/addwork.html', {'jobs': jobs, "form": JobForm(), "error": error})
        else:
            return render(request, 'addwork/addwork.html', {'jobs': jobs, "form": JobForm(),"error":"Not Good"})


def updateall(form_ins):
    jobs= job.objects.filter(name=form_ins.name)
    for worker1 in jobs[0].workers.all():
        worker1.total_hours += form_ins.total_hours
        worker1.total_money += form_ins.total_hours*20
        worker1.own += form_ins.total_hours * 20
        new = ChangeJob()
        new.name = form_ins.name
        new.changehours = form_ins.total_hours
        new.save()
        worker1.jobchange.add(new)
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
        if str(amount).isdigit():
            for job2 in jobs:
                if job2.id == int(job1):
                    job2.money+=int(amount)
                    job2.left=job2.total_amount-job2.money
                    job2.save()
            return render(request, 'updatepayment/updatepaymentforjob.html',
                          {"jobs": jobs[::-1], "switch": switch, "msg": "בוצע בהצלחה"})

        else:
            msg="סכום שגוי , יש להכניס רק ספרות"
            return render(request, 'updatepayment/updatepaymentforjob.html',{"jobs":jobs[::-1],"switch": switch,"msg":msg})



@staff_member_required
def Payment1(request):
    jobs = job.objects.all()
    error=""
    if request.method == "GET":
        return render(request, 'payment/payment.html', {'jobs': jobs, "form": Payment()})
    elif request.method == "POST":
        form = Payment(request.POST)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.save()
            form.save_m2m()
            if len(newForm.workers.all())>0:
                updatepayment(newForm)
            else:
                error="לא נבחרו עובדים"
            newForm.delete()
            return render(request, 'payment/payment.html', {'jobs': jobs, "form": Payment(), "error": error})
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

