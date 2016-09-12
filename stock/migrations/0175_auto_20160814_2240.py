# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0031_auto_20160814_2240'),
        ('stock', '0174_auto_20160814_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='precioventaproducto',
            name='producto',
        ),
        migrations.AlterModelOptions(
            name='productocompuesto',
            options={'verbose_name': 'Productos Compuestos o Elaborados (Recetas)', 'verbose_name_plural': 'Productos Compuestos o Elaborados (Recetas)'},
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_venta',
            field=models.DecimalField(default=1, help_text=b'Ingrese el Precio de Venta del Producto.', verbose_name=b'Precio Venta', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(help_text=b'Seleccione la Categoria del Producto.', to='bar.CategoriaProducto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='codigo_barra',
            field=models.CharField(default=1, help_text=b'Ingrese el codigo de barra del Producto si posee.', max_length=100, verbose_name=b'Codigo de Barra'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='compuesto',
            field=models.BooleanField(default=False, help_text=b'Marque la casilla si el Producto es Compuesto.', verbose_name=b'Es compuesto?'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=models.CharField(default=b'Marca', help_text=b'Ingrese la marca del Producto.', max_length=100, verbose_name=b'Marca'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='subcategoria',
            field=models.ForeignKey(help_text=b'Seleccione la SubCategoria del Producto.', to='bar.SubCategoriaProducto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='unidad_medida_contenido',
            field=models.ForeignKey(related_name='un_med_contenido', default=1, verbose_name=b'Unidad de Medida Contenido', to='bar.UnidadMedidaProducto'),
        ),
        migrations.DeleteModel(
            name='PrecioVentaProducto',
        ),
    ]
