# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0177_auto_20160815_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='codigo_barra',
            field=models.CharField(help_text=b'Ingrese el codigo de barra del Producto si posee.', max_length=100, verbose_name=b'Codigo de Barra'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='compuesto',
            field=models.BooleanField(help_text=b'Marque la casilla si el Producto es Compuesto.', verbose_name=b'Es compuesto?'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='contenido',
            field=models.DecimalField(help_text=b'Ingrese el Contenido del producto de acuerdo a su Unidad de Medida.', verbose_name=b'Cantidad del Contenido', max_digits=10, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=models.CharField(help_text=b'Ingrese la marca del Producto.', max_length=100, verbose_name=b'Marca'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio_venta',
            field=models.DecimalField(help_text=b'Ingrese el Precio de Venta del Producto.', verbose_name=b'Precio Venta', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='unidad_medida_compra',
            field=models.ForeignKey(related_name='un_med_compra', verbose_name=b'Unidad de Medida Compra', to='bar.UnidadMedidaProducto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='unidad_medida_contenido',
            field=models.ForeignKey(related_name='un_med_contenido', verbose_name=b'Unidad de Medida Contenido', to='bar.UnidadMedidaProducto'),
        ),
    ]
