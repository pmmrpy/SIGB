# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0162_auto_20160707_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoEstado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pedido_estado', models.CharField(help_text=b'Ingrese el identificador del Estado del Pedido. (Hasta 3 caracteres)', max_length=3, verbose_name=b'Estado del Pedido', choices=[(b'VIG', b'Vigente'), (b'CAD', b'Caducada'), (b'UTI', b'Utilizada'), (b'CAN', b'Cancelada')])),
                ('descripcion', models.CharField(help_text=b'Ingrese la descripcion del Estado del Pedido. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion del Estado')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Pedido - Estado',
                'verbose_name_plural': 'Pedidos - Estados',
            },
        ),
        migrations.CreateModel(
            name='VentaEstado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('venta_estado', models.CharField(help_text=b'Ingrese el identificador del Estado de la Venta. (Hasta 3 caracteres)', max_length=3, verbose_name=b'Estado de la Venta', choices=[(b'ABI', b'Abierta'), (b'CER', b'Cerrada'), (b'ANU', b'Anulada')])),
                ('descripcion', models.CharField(help_text=b'Ingrese la descripcion del Estado de la Venta. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion del Estado')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Venta - Estado',
                'verbose_name_plural': 'Ventas - Estados',
            },
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 15, 16, 4, 7, 734000, tzinfo=utc), help_text=b'Registra la fecha y hora en la que se definio la Cotizacion. Corresponde a la fecha y hora actual.', verbose_name=b'Fecha de Cotizacion'),
        ),
        migrations.AlterField(
            model_name='reservaestado',
            name='reserva_estado',
            field=models.CharField(help_text=b'Ingrese el identificador del Estado de la Reserva. (Hasta 2 caracteres)', max_length=3, verbose_name=b'Estado de la Reserva', choices=[(b'VIG', b'Vigente'), (b'CAD', b'Caducada'), (b'UTI', b'Utilizada'), (b'CAN', b'Cancelada')]),
        ),
    ]
