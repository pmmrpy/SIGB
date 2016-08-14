# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0162_auto_20160731_2055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterField(
            model_name='precioventaproducto',
            name='fecha_precio_venta_producto',
            field=models.DateTimeField(help_text=b'La fecha y hora se asignan automaticamente al momento de guardar los datos del Precio de Venta del Producto. No se requiere el ingreso de este dato.', verbose_name=b'Fecha registro Precio Venta', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='precioventaproducto',
            name='precio_venta',
            field=models.DecimalField(help_text=b'Ingrese el precio de venta del Producto.', verbose_name=b'Precio Venta', max_digits=20, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo_producto',
            field=models.ForeignKey(verbose_name=b'Tipo de Producto', to='bar.TipoProducto', help_text=b'Seleccione el Tipo de Producto.'),
        ),
    ]
