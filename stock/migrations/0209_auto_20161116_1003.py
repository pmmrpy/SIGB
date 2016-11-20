# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0208_auto_20161116_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productocompuestodetalle',
            name='contenido',
            field=models.DecimalField(help_text=b'Ingrese la cantidad del Producto contenida en el envase de acuerdo a su Unidad de Medida. Los Productos del tipo Insumo comprados a granel (no envasados) siempre deben ser registrados con contenido igual a una unidad. Ej: Queso - 1 kilo, Detergente - 1 litro.', verbose_name=b'Cantidad Contenido', max_digits=10, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='productocompuestodetalle',
            name='producto',
            field=models.ForeignKey(related_name='producto_detalle', verbose_name=b'Nombre del Producto', to='stock.Producto', help_text=b'Seleccione el o los Productos que componen este Producto Compuesto.'),
        ),
        migrations.AlterField(
            model_name='productocompuestodetalle',
            name='producto_compuesto',
            field=models.ForeignKey(related_name='producto_cabecera', to='stock.ProductoCompuesto'),
        ),
        migrations.AlterField(
            model_name='productocompuestodetalle',
            name='unidad_medida_contenido',
            field=models.ForeignKey(related_name='un_med_contenido_prod_compuesto', verbose_name=b'Unidad de Medida Contenido', to='bar.UnidadMedidaProducto', help_text=b'Seleccione la Unidad de Medida del Producto contenido en su presentacion (envase).'),
        ),
    ]
