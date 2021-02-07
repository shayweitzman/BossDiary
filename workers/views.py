from django.shortcuts import render, get_object_or_404,redirect
from workers.models import Worker, Job as job
from workers.forms import JobForm,ReduceHrs,Payment
import datetime
# from django.contrib.auth.decorators import login_required
#
# @login_required

def ReduceHrs1(request):
    jobs = job.objects.all()
    if request.method == "GET":
        return render(request, 'reducehrs/reducehrs.html', {'jobs': jobs, "form": ReduceHrs()})
    elif request.method == "POST":
        form = ReduceHrs(request.POST)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.save()
            form.save_m2m()
            print(newForm.name)
            updatehrs(newForm)
            newForm.delete()
            return redirect("reducehrs")
        else:
            return render(request, 'reducehrs/reducehrs.html', {'jobs': jobs, "form": ReduceHrs(), "error": "Not Good"})


def updatehrs(form_ins):
    jobs = job.objects.filter(name=form_ins.name)
    for worker1 in jobs[0].workers.all():
        if worker1.total_hours-form_ins.total_hours>=0:
            worker1.total_hours -= form_ins.total_hours
            worker1.total_money -= form_ins.total_hours * 20
            worker1.own -= form_ins.total_hours * 20
            print(worker1.own)
            print(worker1.total_hours)
            worker1.save()

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
            print(newForm.name)
            updateall(newForm)
            return redirect("addjob")
        else:
            return render(request, 'addwork/addwork.html', {'jobs': jobs, "form": JobForm(),"error":"Not Good"})

def updateall(form_ins):
    jobs= job.objects.filter(name=form_ins.name)
    for worker1 in jobs[0].workers.all():
        worker1.total_hours += form_ins.total_hours
        worker1.total_money += form_ins.total_hours*20
        worker1.own += form_ins.total_hours * 20
        print(worker1.own)
        print(worker1.total_hours)
        worker1.save()


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
            print(newForm.name)
            updatepayment(newForm)
            newForm.delete()
            return redirect("payment")
        else:
            return render(request, 'payment/payment.html', {'jobs': jobs, "form": Payment(), "error": "Not Good"})


def updatepayment(form_ins):
    jobs = job.objects.filter(name=form_ins.name)
    for worker1 in jobs[0].workers.all():
        worker1.paid += form_ins.money
        worker1.own = worker1.total_money-worker1.paid
        worker1.date=datetime.datetime.now()
        worker1.save()