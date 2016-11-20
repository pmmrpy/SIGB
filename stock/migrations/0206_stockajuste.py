# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0205_inventariodeposito'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockAjuste',
            fields=[
            ],
            options={
                'verbose_name': 'Ajuste de Inventario',
                'proxy': True,
                'verbose_name_plural': 'Stock - Ajustes de Inventario',
            },
            bases=('stock.transferenciastock',),
        ),
    ]
