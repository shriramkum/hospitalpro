# Generated by Django 3.2.3 on 2021-05-18 18:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('patientsapp', '0009_auto_20210518_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 18, 18, 1, 57, 446008, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patients',
            name='disease',
            field=models.CharField(max_length=200),
        ),
    ]
