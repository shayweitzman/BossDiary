# Generated by Django 3.1.6 on 2021-02-07 21:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0019_auto_20210207_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='Money_For_Hour',
            field=models.FloatField(blank=True, default=40, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 7, 23, 51, 34, 892025), null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 7, 23, 51, 34, 892025), null=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 7, 23, 51, 34, 890991), null=True),
        ),
    ]