# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0154_auto_20160729_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precioventaproducto',
            name='fecha_precio_venta_producto',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 30, 18, 56, 4, 150000, tzinfo=utc), help_text=b'Ingrese la fecha y hora en la que se define el precio de venta del producto.'),
        ),
        migrations.AlterField(
            model_name='productocompuesto',
            name='fecha_alta_producto_compuesto',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 30, 18, 56, 4, 151000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Producto. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
        migrations.AlterField(
            model_name='stockdetalle',
            name='fecha_hora_registro_stock',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 30, 18, 56, 4, 153000, tzinfo=utc), help_text=b'Fecha y hora de registro en el Stock.', verbose_name=b'Fecha y hora de registro'),
        ),
    ]
