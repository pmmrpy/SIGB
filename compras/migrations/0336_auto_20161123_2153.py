# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from decimal import Decimal
from django.utils.timezone import utc
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0335_auto_20161121_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compradetalle',
            name='cantidad_producto_compra',
            field=models.DecimalField(help_text=b'Ingrese la cantidad a adquirir del producto.', verbose_name=b'Cantidad Producto', max_digits=10, decimal_places=3, validators=[django.core.validators.MinValueValidator(Decimal('0.001'))]),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 25, 0, 53, 13, 342000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompradetalle',
            name='cantidad_producto_orden_compra',
            field=models.DecimalField(help_text=b'Ingrese la cantidad a adquirir del producto.', verbose_name=b'Cantidad Producto', max_digits=10, decimal_places=3, validators=[django.core.validators.MinValueValidator(Decimal('0.001'))]),
        ),
    ]
