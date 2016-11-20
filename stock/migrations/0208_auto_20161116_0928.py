# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0400_auto_20161116_0928'),
        ('stock', '0207_auto_20161115_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='productocompuestodetalle',
            name='contenido',
            field=models.DecimalField(default=1, help_text=b'Ingrese la cantidad del Producto contenida en el envase de acuerdo a su Unidad de Medida. Los Productos del tipo Insumo comprados a granel (no envasados) siempre deben ser registrados con contenido igual a una unidad. Ej: Queso - 1 kilo, Detergente - 1 litro.', verbose_name=b'Cantidad Contenido', max_digits=10, decimal_places=3),
        ),
        migrations.AddField(
            model_name='productocompuestodetalle',
            name='unidad_medida_contenido',
            field=models.ForeignKey(related_name='un_med_contenido_prod_compuesto', default=1, verbose_name=b'Unidad de Medida Contenido', to='bar.UnidadMedidaProducto', help_text=b'Seleccione la Unidad de Medida del Producto contenido en su presentacion (envase).'),
        ),
    ]
