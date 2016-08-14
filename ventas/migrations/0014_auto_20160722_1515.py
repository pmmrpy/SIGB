# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0152_auto_20160722_1515'),
        ('ventas', '0013_auto_20160722_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidodetalle',
            name='precio_producto_pedido',
            field=models.ForeignKey(default=1, to='stock.PrecioVentaProducto'),
        ),
        migrations.AddField(
            model_name='ventadetalle',
            name='precio_producto_venta',
            field=models.ForeignKey(default=1, to='stock.PrecioVentaProducto'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 22, 19, 15, 15, 457000, tzinfo=utc), help_text=b'', verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='pedidodetalle',
            name='fecha_pedido_detalle',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 22, 19, 15, 15, 458000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha_venta',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 22, 19, 15, 15, 459000, tzinfo=utc)),
        ),
    ]
