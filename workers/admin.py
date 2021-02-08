
from django.contrib import admin
from workers.models import Worker,Job,Payment,ChangeJob

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name','date','total_hours','total_money','own','paid')

class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'total_hours','money')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name','date', 'money')
admin.site.register(ChangeJob)
admin.site.register(Worker,WorkerAdmin)
admin.site.register(Job,JobAdmin)
admin.site.register(Payment,PaymentAdmin)

