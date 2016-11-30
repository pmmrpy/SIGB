# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0225_auto_20161121_1414'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventarioproducto',
            options={'managed': False, 'verbose_name': 'Total Compra/Venta por Producto', 'verbose_name_plural': 'Stock - Totales Compras/Ventas por Productos'},
        ),
        migrations.AlterField(
            model_name='movimientostock',
            name='tipo_movimiento',
            field=models.CharField(help_text=b'Seleccione el identificador del Tipo de Movimiento de Stock.', max_length=2, verbose_name=b'Tipo de Movimiento', choices=[(b'VE', b'Venta'), (b'CO', b'Compra'), (b'TR', b'Transferencias'), (b'AI', b'Ajustes de Inventario'), (b'CP', b'Cancelacion Pedido')]),
        ),
        migrations.AlterField(
            model_name='productocompuestodetalle',
            name='cantidad_insumo',
            field=models.DecimalField(help_text=b'Ingrese la cantidad del Insumo.', verbose_name=b'Cantidad Insumo', max_digits=10, decimal_places=3, validators=[django.core.validators.MinValueValidator(Decimal('0.001'))]),
        ),
    ]
