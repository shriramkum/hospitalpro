# Generated by Django 3.2.3 on 2021-05-17 06:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('patientsapp', '0006_auto_20210516_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 17, 6, 19, 15, 184074, tzinfo=utc)),
        ),
    ]
