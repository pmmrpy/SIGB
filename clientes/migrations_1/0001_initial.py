# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=80)),
                ('apellidos', models.CharField(max_length=80)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.IntegerField(max_length=20)),
                ('telefono_movil', models.IntegerField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
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
                ('documento', models.CharField(max_length=3, serialize=False, primary_key=True, choices=[(b'CI', b'Cedula de Identidad'), (b'RUC', b'Registro Unico del Contribuyente'), (b'P', b'Pasaporte'), (b'RC', b'Registro de Conducir')])),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reserva_fecha_hora', models.DateTimeField()),
                ('reserva_estado', models.CharField(max_length=1, choices=[(b'V', b'Vigente'), (b'C', b'Caducada')])),
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
