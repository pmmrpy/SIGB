# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0058_auto_20161004_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='VentaOcasional',
            fields=[
            ],
            options={
                'verbose_name': 'Venta Ocasional',
                'proxy': True,
                'verbose_name_plural': 'Ventas Ocasionales',
            },
            bases=('ventas.venta',),
        ),
        migrations.CreateModel(
            name='VentaOcasionalDetalle',
            fields=[
            ],
            options={
                'verbose_name': 'Venta Ocasional - Detalle',
                'proxy': True,
                'verbose_name_plural': 'Ventas Ocasionales - Detalles',
            },
            bases=('ventas.ventadetalle',),
        ),
    ]
