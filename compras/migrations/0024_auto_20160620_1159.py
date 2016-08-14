# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0023_auto_20160620_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fecha_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 20, 15, 59, 43, 723000, tzinfo=utc), help_text=b'La fecha y hora se asignan al momento de guardar los datos de la Compra. No se requiere el ingreso de este dato.', verbose_name=b'Fecha y hora de la Compra'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_factura_compra',
            field=models.DateField(default=datetime.datetime(2016, 6, 20, 15, 59, 43, 723000, tzinfo=utc), help_text=b'Ingrese la fecha de la factura.', verbose_name=b'Fecha de la Factura de la Compra'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='fecha_linea_credito_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 20, 15, 59, 43, 720000, tzinfo=utc), help_text=b'Ingrese la fecha en la quese registra la Linea deCredito ofrecida por el Proveedor.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 21, 15, 59, 43, 721000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 20, 15, 59, 43, 721000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de la Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 20, 15, 59, 43, 719000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Proveedor. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
    ]
