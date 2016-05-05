# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_auto_20150918_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=80)),
                ('apellidos', models.CharField(max_length=80)),
                ('fecha_nacimiento', models.DateField(default=datetime.datetime(2015, 9, 28, 2, 1, 54, 24000, tzinfo=utc))),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.IntegerField()),
                ('telefono_movil', models.IntegerField()),
                ('email', models.EmailField(default=b'mail@example.com', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ClienteDocumento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_documento', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('documento', models.CharField(max_length=3)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reserva_fecha_hora', models.DateTimeField()),
                ('reserva_estado', models.CharField(max_length=1)),
                ('reserva_descripcion', models.CharField(default=b'Reserva', max_length=50)),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
                ('mesas', models.ManyToManyField(to='ventas.Mesa')),
            ],
        ),
        migrations.AddField(
            model_name='clientedocumento',
            name='tipo_documento',
            field=models.ForeignKey(to='clientes.Documento'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='documentos',
            field=models.ManyToManyField(to='clientes.Documento', through='clientes.ClienteDocumento'),
        ),
    ]
