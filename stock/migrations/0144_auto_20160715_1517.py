# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0081_auto_20160715_1517'),
        ('ventas', '0006_auto_20160715_1517'),
        ('stock', '0143_auto_20160715_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='producto_ptr',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='producto_stock',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='ubicacion',
        ),
        migrations.AlterField(
            model_name='precioproducto',
            name='fecha_precio_producto',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 15, 19, 17, 1, 427000, tzinfo=utc), help_text=b'Ingrese la fecha y hora en la que se define el precio de venta del producto.'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_alta_producto',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 15, 19, 17, 1, 425000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Producto. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
