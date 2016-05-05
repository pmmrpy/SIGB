# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('mesa', models.ForeignKey(to='ventas.Mesa')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_producto', models.DecimalField(max_digits=20, decimal_places=2)),
                ('pedido', models.ForeignKey(to='ventas.Pedido')),
                ('producto', models.ForeignKey(to='stock.Producto')),
            ],
        ),
    ]
