from workers.models import Worker,Job
from django import forms

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['name','date','total_hours','Money_For_Hour','money','workers']

class AddHrsAndWorkers(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['total_hours','Money_For_Hour','money','workers']


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['name']

class ReduceHrs(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['total_hours','workers']

class Payment(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['name','money','workers']

