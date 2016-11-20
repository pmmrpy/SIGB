# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0405_auto_20161118_1641'),
        ('stock', '0212_remove_insumo_costo_promedio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='insumo',
            options={'verbose_name': 'Insumo', 'verbose_name_plural': 'Productos - Insumos'},
        ),
        migrations.AlterModelOptions(
            name='productocompuestodetalle',
            options={'verbose_name': 'Detalle de Producto Compuesto o Elaborado (Receta)', 'verbose_name_plural': 'Productos - Detalles de Productos Compuestos o Elaborados (Recetas)'},
        ),
        migrations.RemoveField(
            model_name='productocompuestodetalle',
            name='cantidad_producto',
        ),
        migrations.RemoveField(
            model_name='productocompuestodetalle',
            name='contenido',
        ),
        migrations.RemoveField(
            model_name='productocompuestodetalle',
            name='costo_unidad_medida',
        ),
        migrations.RemoveField(
            model_name='productocompuestodetalle',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='productocompuestodetalle',
            name='unidad_medida_contenido',
        ),
        migrations.AddField(
            model_name='insumo',
            name='fecha_alta_insumo',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Insumo. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
        migrations.AddField(
            model_name='insumo',
            name='fecha_modificacion_insumo',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text=b'La Fecha de Modificacion se asigna al momento de guardar los datos modificados del Insumo. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Modificacion'),
        ),
        migrations.AddField(
            model_name='insumo',
            name='unidad_medida',
            field=models.ForeignKey(related_name='un_med_insumo', default=1, verbose_name=b'Unidad de Medida', to='bar.UnidadMedidaProducto', help_text=b'Seleccione la Unidad de Medida del Insumo. Corresponde a la Unidad de Medida en comun para la agrupacion de Productos Insumos para la que sera calculado el costo promedio.'),
        ),
        migrations.AddField(
            model_name='producto',
            name='fecha_modificacion_producto',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text=b'La Fecha de Modificacion se asigna al momento de guardar los datos modificados del Producto. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Modificacion'),
        ),
        migrations.AddField(
            model_name='productocompuestodetalle',
            name='cantidad_insumo',
            field=models.DecimalField(default=1, help_text=b'Ingrese la cantidad del Insumo.', verbose_name=b'Cantidad Insumo', max_digits=10, decimal_places=3),
        ),
        migrations.AddField(
            model_name='productocompuestodetalle',
            name='costo_promedio_insumo',
            field=models.DecimalField(default=0, help_text=b'Corresponde al costo promedio de 1 unidad del Insumo de acuerdo a su Unidad de Medida.', verbose_name=b'Costo Promedio Insumo', max_digits=18, decimal_places=0),
        ),
        migrations.AddField(
            model_name='productocompuestodetalle',
            name='insumo',
            field=models.ForeignKey(related_name='producto_insumo_detalle', default=1, verbose_name=b'Nombre del Insumo', to='stock.Insumo', help_text=b'Seleccione el o los Insumos que componen este Producto Compuesto.'),
        ),
        migrations.AddField(
            model_name='productocompuestodetalle',
            name='unidad_medida_insumo',
            field=models.ForeignKey(related_name='un_med_insumo_prod_compuesto', default=1, verbose_name=b'Unidad de Medida Insumo', to='bar.UnidadMedidaProducto'),
        ),
        migrations.AlterField(
            model_name='insumo',
            name='insumo',
            field=models.CharField(help_text=b'Ingrese el nombre o descripcion del Insumo.', unique=True, max_length=200, verbose_name=b'Nombre del Insumo'),
        ),
        migrations.AlterField(
            model_name='productocompuestodetalle',
            name='total_costo',
            field=models.DecimalField(default=0, help_text=b'Valor calculado entre la Cantidad del Insumo por su Costo Promedio.', verbose_name=b'Total Costo', max_digits=18, decimal_places=0),
        ),
    ]
