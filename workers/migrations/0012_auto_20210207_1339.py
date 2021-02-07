# Generated by Django 3.1.6 on 2021-02-07 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0011_auto_20210207_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='payments',
        ),
        migrations.AddField(
            model_name='payment',
            name='workers',
            field=models.ManyToManyField(blank=True, related_name='payment', to='workers.Worker'),
        ),
        migrations.AlterField(
            model_name='job',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 7, 13, 39, 57, 429003), null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 7, 13, 39, 57, 428005), null=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 7, 13, 39, 57, 428005), null=True),
        ),
    ]
