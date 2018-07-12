# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-11 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReporteDeExistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_reporte', models.DateField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='existencia',
            name='fecha_existencia',
        ),
        migrations.AlterField(
            model_name='existencia',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto', to='inventario.Producto'),
        ),
    ]
