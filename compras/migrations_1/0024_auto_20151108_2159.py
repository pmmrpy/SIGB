# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0023_auto_20151108_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='forma_pago',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='proveedor_compra',
        ),
        migrations.RemoveField(
            model_name='compradetalle',
            name='compra',
        ),
        migrations.RemoveField(
            model_name='compradetalle',
            name='producto',
        ),
        migrations.DeleteModel(
            name='Compra',
        ),
        migrations.DeleteModel(
            name='CompraDetalle',
        ),
    ]
