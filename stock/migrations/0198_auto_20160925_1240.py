# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0197_auto_20160904_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngresoDeposito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('piso', models.CharField(max_length=100)),
                ('pasillo', models.CharField(max_length=100)),
                ('estante', models.CharField(max_length=100)),
                ('nivel', models.CharField(max_length=100)),
                ('producto', models.ForeignKey(to='stock.Producto')),
            ],
            options={
                'verbose_name': 'Ingreso de Producto a Deposito',
                'verbose_name_plural': 'Stock - Ingresos de Productos a Deposito',
            },
        ),
        migrations.DeleteModel(
            name='Devolucion',
        ),
        migrations.DeleteModel(
            name='StockDeposito',
        ),
        migrations.DeleteModel(
            name='StockProducto',
        ),
        migrations.CreateModel(
            name='InventarioProducto',
            fields=[
            ],
            options={
                'db_table': 'inventario_por_producto',
                'verbose_name': 'Inventario por Producto',
                'proxy': True,
                'verbose_name_plural': 'Stock - Inventarios por Productos',
            },
            bases=('stock.stock',),
        ),
    ]
