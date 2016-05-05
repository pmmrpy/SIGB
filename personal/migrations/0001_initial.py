# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=80)),
                ('apellidos', models.CharField(max_length=80)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=50)),
                ('telefono_movil', models.CharField(max_length=50)),
                ('salario', models.DecimalField(max_digits=20, decimal_places=2)),
                ('horario', models.DateTimeField(auto_now=True)),
                ('fecha_nacimiento', models.DateField(default=datetime.datetime(2015, 9, 28, 23, 13, 21, 643000, tzinfo=utc))),
                ('codigo_venta', models.IntegerField()),
                ('email', models.EmailField(default=b'mail@example.com', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='EmpleadoDocumento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_documento', models.CharField(max_length=50)),
                ('empleado', models.ForeignKey(to='personal.Empleado')),
                ('tipo_documento', models.ForeignKey(to='bar.Documento')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horario', models.CharField(max_length=30)),
                ('horario_inicio', models.TimeField(default=datetime.datetime(2015, 9, 28, 23, 13, 21, 646000, tzinfo=utc))),
                ('horario_fin', models.TimeField(default=datetime.datetime(2015, 9, 28, 23, 13, 21, 646000, tzinfo=utc))),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='documentos',
            field=models.ManyToManyField(to='bar.Documento', through='personal.EmpleadoDocumento'),
        ),
    ]
