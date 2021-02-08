# Generated by Django 3.1.6 on 2021-02-08 13:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0022_auto_20210208_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changejob',
            name='name',
            field=models.CharField(default=0, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 8, 15, 54, 34, 372641), null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 8, 15, 54, 34, 372641), null=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 8, 15, 54, 34, 371643), null=True),
        ),
    ]