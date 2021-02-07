# Generated by Django 3.1.6 on 2021-02-07 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0016_auto_20210207_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='left',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='total_amount',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 7, 18, 28, 12, 432760), null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 7, 18, 28, 12, 431762), null=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 7, 18, 28, 12, 430765), null=True),
        ),
    ]