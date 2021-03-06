# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('error_id', models.AutoField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('date_time', models.DateTimeField()),
                ('message_id', models.IntegerField(max_length=16)),
                ('error_message', models.CharField(max_length=256)),
                ('error_temperature', models.DecimalField(decimal_places=2, max_digits=16)),
                ('error_humidity', models.DecimalField(decimal_places=2, max_digits=16)),
                ('error_co2', models.IntegerField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('measurement_id', models.AutoField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('date_time', models.DateTimeField()),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=16)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=16)),
                ('co2', models.IntegerField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('user_name', models.CharField(max_length=256, unique=True)),
                ('password_hash', models.CharField(max_length=256)),
            ],
        ),
    ]
