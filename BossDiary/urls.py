"""LibraryProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from homepage import views as homepage_views
from workers import views as workers_views
from reports import views as reports_views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', homepage_views.homepage, name='homepage'),
    path('addjob/',workers_views.Job,name='addjob'),
    path('addworker/',workers_views.AddWorker,name='addworker'),
    path('reducehrs/',workers_views.ReduceHrs1,name='reducehrs'),
    path('Payment/',workers_views.Payment1,name='payment'),
    path('Reports/',reports_views.reports1,name='reports'),
    path('jobspermonth/',reports_views.jobspermonth,name='jobspermonth'),
    path('payments/',reports_views.paymentreport,name='paymentreport'),
    path('jobspermonth/',reports_views.jobspermonth,name='jobspermonth'),
    path('paymentspermonth/',reports_views.paymentspermonth,name='paymentspermonth'),
    path('paymentsperworker/',reports_views.paymentperworker,name='paymentperworker'),
    path('updatepayment/',workers_views.updatepaymentforjob,name='updatepaymentforjob'),
    path('addhrsandworkers/',workers_views.addhrsandworkers,name='addhrsandworkers'),
    path('jobsperworker',reports_views.jobsperuser,name='jobsperuser'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
