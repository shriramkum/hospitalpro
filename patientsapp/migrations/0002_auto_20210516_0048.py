# Generated by Django 2.0 on 2021-05-15 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
