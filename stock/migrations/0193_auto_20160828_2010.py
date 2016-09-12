# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0192_auto_20160827_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='contenido',
            field=models.DecimalField(help_text=b'Ingrese la cantidad del Producto contenida en el envase de acuerdo a su Unidad de Medida. Los Productos comprados a granel (no envasados) siempre deben ser registrados con contenido igual a una unidad. Ej: Queso - 1 kilo, Detergente - 1 litro.', verbose_name=b'Cantidad Contenido', max_digits=10, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='producto',
            name='porcentaje_ganancia',
            field=models.DecimalField(default=0, help_text=b'Ingrese el Porcentaje de Ganancia o Margen de Utilidad que desea obtener de la venta del Producto.', verbose_name=b'Porcentaje de Ganancia', max_digits=3, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio_compra_sugerido',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula promediando el Costo de Compra del Producto en el ultimo mes.', verbose_name=b'Precio Compra Sugerido', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='unidad_medida_compra',
            field=models.ForeignKey(related_name='un_med_compra', verbose_name=b'Unidad de Medida Compra', to='bar.UnidadMedidaProducto', help_text=b'Seleccione la Unidad de Medida con el cual el Producto es adquirido. Corresponde a la Unidad de Medida de la presentacion del Producto.'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='unidad_medida_contenido',
            field=models.ForeignKey(related_name='un_med_contenido', verbose_name=b'Unidad de Medida Contenido', to='bar.UnidadMedidaProducto', help_text=b'Seleccione la Unidad de Medida del Producto contenido en su presentacion (envase).'),
        ),
    ]
