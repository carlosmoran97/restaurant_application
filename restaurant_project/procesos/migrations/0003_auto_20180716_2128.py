# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-16 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procesos', '0002_auto_20180716_0147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orden',
            name='descuento',
        ),
        migrations.AddField(
            model_name='detalleorden',
            name='descuento',
            field=models.FloatField(null=True),
        ),
    ]
