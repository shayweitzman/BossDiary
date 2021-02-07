from django.db import models
from django.contrib.auth.models import User
import datetime




class Worker (models.Model):
    name = models.CharField(max_length=50,unique=True)
    date = models.DateField(default=datetime.datetime.now(), null=True, blank=True)
    total_hours = models.FloatField(default=0, null=True, blank=True)
    total_money = models.FloatField(default=0, null=True, blank=True)
    own = models.FloatField(default=0, null=True, blank=True)
    paid = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name


class Payment(models.Model):
    money = models.FloatField(max_length=50)
    date = models.DateField(default=datetime.datetime.now(), null=True, blank=True)
    workers = models.ManyToManyField(Worker, blank=True, related_name='payment')
    name = models.CharField(max_length=50,null=True, blank=True,default=None)

    def __str__(self):
        return str(self.date)

class Job(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(default=datetime.datetime.now(), null=True, blank=True)
    total_hours=models.FloatField(default=0,null=True,blank=True)
    money = models.FloatField(default=0, null=True, blank=True)
    workers = models.ManyToManyField(Worker, blank=True, related_name='workerjobs')

    def __str__(self):
        return self.name

