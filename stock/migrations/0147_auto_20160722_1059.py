# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0146_auto_20160718_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='precioproducto',
            options={'ordering': ('-fecha_precio_producto',), 'verbose_name': 'Producto - Precio de Venta', 'verbose_name_plural': 'Productos - Precios de Venta'},
        ),
        migrations.AlterField(
            model_name='precioproducto',
            name='fecha_precio_producto',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 22, 14, 59, 6, 170000, tzinfo=utc), help_text=b'Ingrese la fecha y hora en la que se define el precio de venta del producto.'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(help_text=b'Seleccione el archivo con la imagen del Producto.', upload_to=b'stock/productos/', verbose_name=b'Archivo de Imagen'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='cantidad_entrante',
            field=models.DecimalField(help_text=b'Cantidad entrante al Stock del producto.', verbose_name=b'Cantidad Entrante', max_digits=10, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='stock',
            name='cantidad_existente',
            field=models.DecimalField(help_text=b'Cantidad existente en Stock.', verbose_name=b'Cantidad Existente', max_digits=10, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='stock',
            name='cantidad_saliente',
            field=models.DecimalField(help_text=b'Cantidad saliente del Stock del producto.', verbose_name=b'Cantidad Saliente', max_digits=10, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='stock',
            name='fecha_hora_registro_stock',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 22, 14, 59, 6, 170000, tzinfo=utc), help_text=b'Fecha y hora de registro en el Stock.', verbose_name=b'Fecha y hora de registro'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='producto_stock',
            field=models.ForeignKey(related_name='producto_stock', verbose_name=b'Producto', to='stock.Producto'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='ubicacion',
            field=models.ForeignKey(help_text=b'Ubicacion del Stock.', to='bar.Deposito'),
        ),
    ]
