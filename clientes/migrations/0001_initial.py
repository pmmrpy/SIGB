# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0001_initial'),
        ('ventas', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=80)),
                ('apellidos', models.CharField(max_length=80)),
                ('fecha_nacimiento', models.DateField(default=datetime.datetime(2015, 9, 28, 23, 12, 58, 175000, tzinfo=utc))),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=50)),
                ('telefono_movil', models.CharField(max_length=50)),
                ('email', models.EmailField(default=b'mail@example.com', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ClienteDocumento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_documento', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
                ('tipo_documento', models.ForeignKey(to='bar.Documento')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(default=b'Reserva de Mesa', max_length=50)),
                ('fecha_hora', models.DateTimeField(default=datetime.datetime(2015, 9, 28, 23, 12, 58, 178000, tzinfo=utc))),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
                ('estado', models.ForeignKey(to='bar.ReservaEstado')),
                ('mesas', models.ManyToManyField(to='ventas.Mesa')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='documentos',
            field=models.ManyToManyField(to='bar.Documento', through='clientes.ClienteDocumento'),
        ),
    ]
