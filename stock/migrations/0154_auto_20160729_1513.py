# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0153_auto_20160726_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precioventaproducto',
            name='fecha_precio_venta_producto',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 29, 19, 13, 50, 378000, tzinfo=utc), help_text=b'Ingrese la fecha y hora en la que se define el precio de venta del producto.'),
        ),
        migrations.AlterField(
            model_name='productocompuesto',
            name='fecha_alta_producto_compuesto',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 29, 19, 13, 50, 379000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Producto. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
        migrations.AlterField(
            model_name='stockdetalle',
            name='fecha_hora_registro_stock',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 29, 19, 13, 50, 381000, tzinfo=utc), help_text=b'Fecha y hora de registro en el Stock.', verbose_name=b'Fecha y hora de registro'),
        ),
    ]
