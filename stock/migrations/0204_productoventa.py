# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0203_producto_tiempo_elaboracion'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoVenta',
            fields=[
            ],
            options={
                'verbose_name': 'Producto para la Venta',
                'proxy': True,
                'verbose_name_plural': 'Productos - Productos para la Venta',
            },
            bases=('stock.producto',),
        ),
    ]
