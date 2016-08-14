# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_auto_20151025_1138'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedidodetalle',
            options={'verbose_name': 'Pedido - Detalle', 'verbose_name_plural': 'Pedidos - Detalles'},
        ),
    ]
