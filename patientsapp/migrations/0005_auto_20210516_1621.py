# Generated by Django 2.0 on 2021-05-16 10:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('patientsapp', '0004_auto_20210516_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 16, 10, 51, 13, 6721, tzinfo=utc)),
        ),
    ]
