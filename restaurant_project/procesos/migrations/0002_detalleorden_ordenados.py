# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-19 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procesos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleorden',
            name='ordenados',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
