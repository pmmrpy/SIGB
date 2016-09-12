# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0189_auto_20160826_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='costo_elaboracion',
            field=models.DecimalField(default=0, help_text=b'Suma de .', verbose_name=b'Costo de Elaboracion del Producto', max_digits=18, decimal_places=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_venta_sugerido',
            field=models.DecimalField(default=0, help_text=b'Precio de Venta sugerido calculado a partir del promedio del Costo de Compra del producto del ultimo mes por el Porcentaje de Ganancia.', verbose_name=b'Precio Venta Sugerido', max_digits=18, decimal_places=0),
        ),
        migrations.AddField(
            model_name='productocompuestodetalle',
            name='costo_unidad_medida',
            field=models.DecimalField(default=0, help_text=b'Corresponde al costo de 1 unidad del Producto de acuerdo a su Unidad de Medida del Contenido.', verbose_name=b'Costo por Unidad de Medida', max_digits=18, decimal_places=0),
        ),
        migrations.AddField(
            model_name='productocompuestodetalle',
            name='total_costo',
            field=models.DecimalField(default=0, help_text=b'Valor calculado entre la Cantidad del Producto por el Costo por Unidad de Medida del Producto.', verbose_name=b'Total Costo', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='porcentaje_ganancia',
            field=models.DecimalField(default=30, help_text=b'Ingrese el Margen de Utilidad o Porcentaje de Ganancia que desea obtener de la venta del Producto.', verbose_name=b'Porcentaje de Ganancia', max_digits=3, decimal_places=0),
        ),
    ]
