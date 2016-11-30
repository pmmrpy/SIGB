# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0222_ajustestock_ajustestockdetalle'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockDepositoAjusteInventario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('producto', models.CharField(max_length=100)),
                ('deposito_id', models.PositiveIntegerField()),
                ('cantidad_existente', models.IntegerField(verbose_name=b'Cantidad Existente')),
            ],
            options={
                'verbose_name': 'Stock por Deposito para Ajuste de Inventario',
                'db_table': 'stock_por_deposito_para_ajuste_inventario',
                'managed': False,
                'verbose_name_plural': 'Stock - Stock por Depositos para Ajustes de Inventario',
            },
        ),
    ]
