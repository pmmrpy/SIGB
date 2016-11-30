# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0224_auto_20161120_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ajustestockdetalle',
            name='cantidad_ajustar_producto',
            field=models.DecimalField(decimal_places=3, validators=[django.core.validators.MinValueValidator(Decimal('0.001'))], max_digits=10, blank=True, help_text=b'Ingrese la cantidad a ajustar del Producto. Debe ingresar la cantidad del Producto que finalmente quedara registrada en el Inventario.', null=True, verbose_name=b'Cantidad Ajuste'),
        ),
        migrations.AlterField(
            model_name='transferenciastockdetalle',
            name='cantidad_producto_transferencia',
            field=models.DecimalField(help_text=b'Ingrese la cantidad a transferir del Producto.', verbose_name=b'Cantidad a transferir', max_digits=10, decimal_places=3, validators=[django.core.validators.MinValueValidator(Decimal('0.001'))]),
        ),
    ]
