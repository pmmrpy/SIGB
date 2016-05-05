# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_auto_20150918_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='CajaEstado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caja_estado', models.CharField(max_length=3)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CajaUbicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ubicacion', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MesaEstado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mesa_estado', models.CharField(max_length=3)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MesaUbicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ubicacion', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='caja',
            name='estado',
            field=models.ForeignKey(to='ventas.CajaEstado'),
        ),
        migrations.AlterField(
            model_name='caja',
            name='ubicacion',
            field=models.ForeignKey(to='ventas.CajaUbicacion'),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='estado',
            field=models.ForeignKey(to='ventas.MesaEstado'),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='ubicacion',
            field=models.ForeignKey(to='ventas.MesaUbicacion'),
        ),
    ]
