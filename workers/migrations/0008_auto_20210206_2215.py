# Generated by Django 3.1.6 on 2021-02-06 20:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0007_auto_20210206_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 6, 22, 15, 47, 627019), null=True),
        ),
    ]
