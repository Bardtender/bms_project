# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 17:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('headstation', '0002_auto_20171013_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='errorlog',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='sensordata',
            name='date_time',
        ),
    ]