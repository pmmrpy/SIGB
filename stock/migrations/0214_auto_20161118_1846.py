# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0213_auto_20161118_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumo',
            name='fecha_alta_insumo',
            field=models.DateTimeField(help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Insumo. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='insumo',
            name='fecha_modificacion_insumo',
            field=models.DateTimeField(help_text=b'La Fecha de Modificacion se asigna al momento de guardar los datos modificados del Insumo. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Modificacion', auto_now=True),
        ),
        migrations.AlterField(
            model_name='insumo',
            name='unidad_medida',
            field=models.ForeignKey(related_name='un_med_insumo', verbose_name=b'Unidad de Medida', to='bar.UnidadMedidaProducto', help_text=b'Seleccione la Unidad de Medida del Insumo. Corresponde a la Unidad de Medida en comun para la agrupacion de Productos Insumos para la que sera calculado el costo promedio.'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_modificacion_producto',
            field=models.DateTimeField(help_text=b'La Fecha de Modificacion se asigna al momento de guardar los datos modificados del Producto. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Modificacion', auto_now=True),
        ),
        migrations.AlterField(
            model_name='productocompuestodetalle',
            name='costo_promedio_insumo',
            field=models.DecimalField(help_text=b'Corresponde al costo promedio de 1 unidad del Insumo de acuerdo a su Unidad de Medida.', verbose_name=b'Costo Promedio Insumo', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='productocompuestodetalle',
            name='insumo',
            field=models.ForeignKey(related_name='producto_insumo_detalle', verbose_name=b'Nombre del Insumo', to='stock.Insumo', help_text=b'Seleccione el o los Insumos que componen este Producto Compuesto.'),
        ),
        migrations.AlterField(
            model_name='productocompuestodetalle',
            name='total_costo',
            field=models.DecimalField(help_text=b'Valor calculado entre la Cantidad del Insumo por su Costo Promedio.', verbose_name=b'Total Costo', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='productocompuestodetalle',
            name='unidad_medida_insumo',
            field=models.ForeignKey(related_name='un_med_insumo_prod_compuesto', verbose_name=b'Unidad de Medida Insumo', to='bar.UnidadMedidaProducto'),
        ),
    ]
