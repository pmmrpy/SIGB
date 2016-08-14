# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0005_auto_20160601_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordencompra',
            name='numero_orden_compra',
            field=models.UUIDField(default=uuid.uuid4, help_text=b'Este dato se genera automaticamente cada vez que se va crear una Orden de Compra.', verbose_name=b'Numero de Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 1, 17, 56, 33, 710000, tzinfo=utc), help_text=b'La fecha y hora se asignan al momento de guardar los datos de la Compra. No se requiere el ingreso de este dato.'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='fecha_linea_credito_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 1, 17, 56, 33, 707000, tzinfo=utc), help_text=b'Ingrese la fecha en la quese registra la Linea deCredito ofrecida por el Proveedor.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 2, 17, 56, 33, 708000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 1, 17, 56, 33, 708000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 1, 17, 56, 33, 706000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Proveedor. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
    ]
