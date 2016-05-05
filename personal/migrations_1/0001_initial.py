# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=80)),
                ('apellidos', models.CharField(max_length=80)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.IntegerField(max_length=20)),
                ('telefono_movil', models.IntegerField(max_length=20)),
                ('salario', models.DecimalField(max_digits=20, decimal_places=2)),
                ('horario', models.DateTimeField(auto_now=True)),
                ('codigo_venta', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='EmpleadoDocumento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_documento', models.CharField(max_length=50)),
                ('empleado', models.ForeignKey(to='personal.Empleado')),
                ('tipo_documento', models.ForeignKey(to='clientes.Documento')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('horario', models.CharField(max_length=30, serialize=False, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='documentos',
            field=models.ManyToManyField(to='clientes.Documento', through='personal.EmpleadoDocumento'),
        ),
    ]
