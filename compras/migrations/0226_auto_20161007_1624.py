# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0225_auto_20161004_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturaproveedor',
            name='orden_compra',
            field=models.ForeignKey(default=18, verbose_name=b'Nro. Orden Compra', to='compras.OrdenCompra', help_text=b'Seleccione la Orden de Compra cuya Factura sera registrada.'),
        ),
        migrations.AddField(
            model_name='ordenpagodetalle',
            name='orden_compra',
            field=models.ForeignKey(default=18, verbose_name=b'Nro. Orden Compra', to='compras.OrdenCompra', help_text=b'Seleccione la Orden de Compra cuya Factura sera registrada.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 8, 19, 24, 5, 37000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
    ]
