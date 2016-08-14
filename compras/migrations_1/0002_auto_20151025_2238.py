# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_auto_20151025_1834'),
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoProveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('producto', models.ForeignKey(to='stock.Producto')),
                ('proveedor', models.ForeignKey(to='compras.Proveedor')),
            ],
        ),
        migrations.AddField(
            model_name='compradetalle',
            name='total_compra',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='cantidad_producto',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='producto',
            field=models.ForeignKey(related_name='productos', to='compras.ProductoProveedor'),
        ),
    ]
