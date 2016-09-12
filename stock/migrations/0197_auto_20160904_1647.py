# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0196_auto_20160831_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='contenido',
            field=models.DecimalField(help_text=b'Ingrese la cantidad del Producto contenida en el envase de acuerdo a su Unidad de Medida. Los Productos del tipo Insumo comprados a granel (no envasados) siempre deben ser registrados con contenido igual a una unidad. Ej: Queso - 1 kilo, Detergente - 1 litro.', verbose_name=b'Cantidad Contenido', max_digits=10, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio_compra',
            field=models.DecimalField(default=0, help_text=b'Corresponde al valor del Precio de Compra almacenado en la Base de Datos del Sistema. Este valor sera utilizado para operaciones a realizar con el Producto.', verbose_name=b'Precio Compra', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio_venta',
            field=models.DecimalField(default=0, help_text=b'Corresponde al valor del Precio de Venta almacenado en la Base de Datos del Sistema. Este valor sera utilizado para operaciones a realizar con el Producto.', verbose_name=b'Precio Venta', max_digits=18, decimal_places=0),
        ),
    ]
