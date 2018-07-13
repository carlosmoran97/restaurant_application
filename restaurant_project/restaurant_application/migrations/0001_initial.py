# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-13 03:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salario', models.DecimalField(decimal_places=2, max_digits=20)),
                ('fecha_contratacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaPlatillo',
            fields=[
                ('idCategoriaPlatillo', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('idEmpleado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateField()),
                ('dui', models.CharField(max_length=9)),
                ('nit', models.CharField(max_length=14)),
                ('afp', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('codigo_mesa', models.AutoField(primary_key=True, serialize=False)),
                ('numero_mesa', models.IntegerField()),
                ('asientos', models.IntegerField()),
                ('ocupado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Platillo',
            fields=[
                ('codigoPlatillo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('precioUnitario', models.DecimalField(decimal_places=2, max_digits=20)),
                ('categoria_platillo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='platillo', to='restaurant_application.CategoriaPlatillo')),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('idPuesto', models.AutoField(primary_key=True, serialize=False)),
                ('puesto', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='asignacion',
            name='empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignacion_empleado', to='restaurant_application.Empleado'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='puesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignacion_puesto', to='restaurant_application.Puesto'),
        ),
        migrations.AlterUniqueTogether(
            name='asignacion',
            unique_together=set([('empleado', 'puesto')]),
        ),
    ]
