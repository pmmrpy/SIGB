# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0198_auto_20160925_1240'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InventarioProducto',
        ),
        migrations.CreateModel(
            name='InventarioProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('producto', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Inventario por Producto',
                'db_table': 'inventario_por_producto',
                'managed': False,
                'verbose_name_plural': 'Stock - Inventarios por Productos',
            },
        ),
    ]
