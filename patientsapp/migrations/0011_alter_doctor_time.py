# Generated by Django 3.2.3 on 2021-05-19 19:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('patientsapp', '0010_auto_20210518_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 19, 19, 12, 32, 858611, tzinfo=utc)),
        ),
    ]
