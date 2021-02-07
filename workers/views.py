from django.shortcuts import render, get_object_or_404,redirect
from workers.models import Worker as worker ,Payment as paymentmodel ,Job as job
from workers.forms import JobForm,ReduceHrs,Payment,WorkerForm
import datetime
from django.contrib.admin.views.decorators import staff_member_required



@staff_member_required
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
        # worker1.payments.add(payment)

