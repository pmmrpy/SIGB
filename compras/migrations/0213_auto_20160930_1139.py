# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0212_auto_20160930_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facturaproveedor',
            name='estado_factura_compra',
        ),
        migrations.RemoveField(
            model_name='ordenpago',
            name='estado_orden_pago',
        ),
        migrations.RemoveField(
            model_name='ordenpagodetalle',
            name='estado_factura_compra',
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 1, 15, 39, 36, 242000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
    ]
