# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0009_auto_20160601_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordencompra',
            name='estado_orden_compra',
        ),
        migrations.RemoveField(
            model_name='ordencompra',
            name='forma_pago_orden_compra',
        ),
        migrations.RemoveField(
            model_name='ordencompra',
            name='proveedor_orden_compra',
        ),
        migrations.RemoveField(
            model_name='ordencompradetalle',
            name='ordencompra',
        ),
        migrations.RemoveField(
            model_name='ordencompradetalle',
            name='producto_orden_compra',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='numero_orden_compra',
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 1, 18, 41, 45, 385000, tzinfo=utc), help_text=b'La fecha y hora se asignan al momento de guardar los datos de la Compra. No se requiere el ingreso de este dato.'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='fecha_linea_credito_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 1, 18, 41, 45, 382000, tzinfo=utc), help_text=b'Ingrese la fecha en la quese registra la Linea deCredito ofrecida por el Proveedor.'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 1, 18, 41, 45, 381000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Proveedor. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
        migrations.DeleteModel(
            name='OrdenCompra',
        ),
        migrations.DeleteModel(
            name='OrdenCompraDetalle',
        ),
    ]
