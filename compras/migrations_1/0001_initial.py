# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CompraDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_producto', models.DecimalField(max_digits=20, decimal_places=2)),
                ('precio_compra_producto', models.DecimalField(max_digits=20, decimal_places=2)),
                ('total_compra_producto', models.DecimalField(max_digits=20, decimal_places=2)),
                ('compra', models.ForeignKey(to='compras.Compra')),
                ('producto', models.ForeignKey(to='stock.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('proveedor', models.CharField(max_length=100)),
                ('ruc', models.CharField(max_length=12)),
                ('telefono', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(to='compras.Proveedor'),
        ),
    ]
