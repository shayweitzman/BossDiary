# Generated by Django 3.1.6 on 2021-02-07 12:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0012_auto_20210207_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 7, 14, 18, 56, 860582), null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 7, 14, 18, 56, 859586), null=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 7, 14, 18, 56, 859586), null=True),
        ),
    ]
