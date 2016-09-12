# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0179_auto_20160816_1318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='confirmatransferenciastock',
            options={'verbose_name': 'Confirmacion de Transferencia de Producto entre Deposito', 'verbose_name_plural': 'Stock - Confirmaciones de Transferencias de Productos entre Depositos'},
        ),
        migrations.AlterModelOptions(
            name='productocompuesto',
            options={'verbose_name': 'Producto Compuesto o Elaborado (Receta)', 'verbose_name_plural': 'Productos - Compuestos o Elaborados (Recetas)'},
        ),
        migrations.AlterModelOptions(
            name='solicitatransferenciastock',
            options={'verbose_name': 'Solicitud de Transferencia de Producto entre Deposito', 'verbose_name_plural': 'Stock - Solicitudes de Transferencias de Productos entre Depositos'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name': 'Inventario de Producto', 'verbose_name_plural': 'Productos - Inventarios'},
        ),
        migrations.AlterModelOptions(
            name='stockdetalle',
            options={'verbose_name': 'Detalle de Inventario del Producto', 'verbose_name_plural': 'Productos - Detalles de Inventarios'},
        ),
        migrations.AlterField(
            model_name='transferenciastock',
            name='estado_transferencia',
            field=models.ForeignKey(default=1, to='bar.TransferenciaStockEstado'),
        ),
    ]
