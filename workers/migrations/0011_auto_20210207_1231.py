# Generated by Django 3.1.6 on 2021-02-07 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0010_auto_20210207_0059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.FloatField(max_length=50)),
                ('date', models.DateField(blank=True, default=datetime.datetime(2021, 2, 7, 12, 31, 54, 157972), null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 7, 12, 31, 54, 158969), null=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 7, 12, 31, 54, 157972), null=True),
        ),
        migrations.AddField(
            model_name='worker',
            name='payments',
            field=models.ManyToManyField(blank=True, related_name='payment', to='workers.Payment'),
        ),
    ]