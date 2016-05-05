# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0002_categoriaproducto_formapago'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deposito', models.CharField(max_length=3)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PrecioProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('precio_venta', models.DecimalField(max_digits=20, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('producto', models.CharField(max_length=100)),
                ('codigo_barra', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('categoria', models.ForeignKey(to='bar.CategoriaProducto')),
                ('precio_venta', models.ForeignKey(related_name='precio', to='stock.PrecioProducto')),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('receta', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='RecetaDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_producto', models.DecimalField(max_digits=20, decimal_places=2)),
                ('producto', models.ForeignKey(to='stock.Producto')),
                ('receta', models.ForeignKey(to='stock.Receta')),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeposito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_deposito', models.CharField(max_length=2)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unidad_medida', models.CharField(max_length=2)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='receta',
            name='productos',
            field=models.ManyToManyField(to='stock.Producto', through='stock.RecetaDetalle'),
        ),
        migrations.AddField(
            model_name='producto',
            name='unidad_medida',
            field=models.ForeignKey(to='stock.UnidadMedida'),
        ),
        migrations.AddField(
            model_name='precioproducto',
            name='producto',
            field=models.ForeignKey(to='stock.Producto'),
        ),
        migrations.AddField(
            model_name='deposito',
            name='tipo_deposito',
            field=models.ForeignKey(to='stock.TipoDeposito'),
        ),
    ]
