# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField()),
            ],
        ),
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
            name='Mesa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
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
        migrations.AddField(
            model_name='mesa',
            name='estado',
            field=models.ForeignKey(to='ventas.MesaEstado'),
        ),
        migrations.AddField(
            model_name='mesa',
            name='ubicacion',
            field=models.ForeignKey(to='ventas.MesaUbicacion'),
        ),
        migrations.AddField(
            model_name='caja',
            name='estado',
            field=models.ForeignKey(to='ventas.CajaEstado'),
        ),
        migrations.AddField(
            model_name='caja',
            name='ubicacion',
            field=models.ForeignKey(to='ventas.CajaUbicacion'),
        ),
    ]
