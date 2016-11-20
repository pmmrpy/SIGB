# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0206_stockajuste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='costo_elaboracion',
            field=models.DecimalField(default=0, help_text=b'Suma de los Totales de Costo del detalle del Producto Compuesto.', verbose_name=b'Costo de Elaboracion', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='productocompuestodetalle',
            name='producto',
            field=models.ForeignKey(related_name='producto_detalle', default=15, verbose_name=b'Nombre del Producto', to='stock.Producto', help_text=b'Seleccione el o los Productos que componen este Producto Compuesto.'),
        ),
        migrations.AlterField(
            model_name='productocompuestodetalle',
            name='producto_compuesto',
            field=models.ForeignKey(related_name='producto_cabecera', default=49, to='stock.ProductoCompuesto'),
        ),
    ]
