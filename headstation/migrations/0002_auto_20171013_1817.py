# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headstation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errorlog',
            name='error_co2',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='error_humidity',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='error_temperature',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='message_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='co2',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='humidity',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='temperature',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
