# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0190_auto_20160827_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='costo_elaboracion',
            field=models.DecimalField(default=0, help_text=b'Suma de los Totales de Costo del detalle del Producto Compuesto.', verbose_name=b'Costo de Elaboracion del Producto', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio_venta_sugerido',
            field=models.DecimalField(default=0, help_text=b'Precio de Venta sugerido calculado a partir del promedio del Costo de Compra del producto en el ultimo mes por el Porcentaje de Ganancia.', verbose_name=b'Precio Venta Sugerido', max_digits=18, decimal_places=0),
        ),
    ]
