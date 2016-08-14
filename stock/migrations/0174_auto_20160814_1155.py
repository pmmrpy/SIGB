# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0173_productocompuestodetalle_producto_compuesto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='contenido',
            field=models.DecimalField(default=0, help_text=b'Ingrese el Contenido del producto de acuerdo a su Unidad de Medida.', verbose_name=b'Cantidad del Contenido', max_digits=10, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='producto',
            name='unidad_medida_contenido',
            field=models.ForeignKey(related_name='un_med_contenido', verbose_name=b'Unidad de Medida Contenido', to='bar.UnidadMedidaProducto', null=True),
        ),
    ]
