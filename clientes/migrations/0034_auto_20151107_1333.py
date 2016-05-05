# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0009_auto_20151107_1333'),
        ('clientes', '0033_auto_20151107_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelefonoCliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telefono', models.IntegerField(help_text=b'Ingrese el telefono del cliente. El dato debe contener solo numeros.')),
            ],
        ),
        migrations.CreateModel(
            name='TelefonoMovilCliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telefono_movil', models.IntegerField(help_text=b'Ingrese el telefono movil del cliente. El dato debe contener solo numeros.')),
            ],
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='telefono_movil',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 11, 7, 16, 33, 30, 121000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 16, 33, 30, 128000, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='telefonomovilcliente',
            name='cliente',
            field=models.ForeignKey(to='clientes.Cliente'),
        ),
        migrations.AddField(
            model_name='telefonomovilcliente',
            name='codigo_ciudad_operadora_telefono',
            field=models.ForeignKey(default=21, to='bar.CodigoCiudadOperadoraTelefono'),
        ),
        migrations.AddField(
            model_name='telefonomovilcliente',
            name='codigo_pais_telefono',
            field=models.ForeignKey(default=595, to='bar.CodigoPaisTelefono'),
        ),
        migrations.AddField(
            model_name='telefonocliente',
            name='cliente',
            field=models.ForeignKey(to='clientes.Cliente'),
        ),
        migrations.AddField(
            model_name='telefonocliente',
            name='codigo_ciudad_operadora_telefono',
            field=models.ForeignKey(default=21, to='bar.CodigoCiudadOperadoraTelefono'),
        ),
        migrations.AddField(
            model_name='telefonocliente',
            name='codigo_pais_telefono',
            field=models.ForeignKey(default=595, to='bar.CodigoPaisTelefono'),
        ),
    ]
