# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0176_devolucion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productocompuesto',
            options={'verbose_name': 'Producto - Compuesto o Elaborado (Receta)', 'verbose_name_plural': 'Productos - Compuestos o Elaborados (Recetas)'},
        ),
        migrations.AlterModelOptions(
            name='productocompuestodetalle',
            options={'verbose_name': 'Producto - Detalle de Compuesto o Elaborado (Receta)', 'verbose_name_plural': 'Productos - Detalles de Compuestos o Elaborados (Recetas)'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name': 'Producto - Inventario', 'verbose_name_plural': 'Productos - Inventarios'},
        ),
        migrations.AlterModelOptions(
            name='stockdetalle',
            options={'verbose_name': 'Producto - Detalle de Inventario', 'verbose_name_plural': 'Productos - Detalles de Inventarios'},
        ),
    ]
