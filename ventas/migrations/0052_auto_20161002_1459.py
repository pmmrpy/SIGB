# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0301_auto_20161002_1459'),
        ('ventas', '0051_auto_20161002_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comanda',
            name='producto_a_elaborar',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='apertura_caja',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='cliente_factura',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='estado_venta',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='numero_factura_venta',
        ),
        migrations.RemoveField(
            model_name='ventadetalle',
            name='producto_venta',
        ),
        migrations.RemoveField(
            model_name='ventadetalle',
            name='venta',
        ),
        migrations.DeleteModel(
            name='Comanda',
        ),
        migrations.DeleteModel(
            name='Venta',
        ),
        migrations.DeleteModel(
            name='VentaDetalle',
        ),
    ]
