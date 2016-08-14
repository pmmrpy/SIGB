# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0101_auto_20160616_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategoriaProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subcategoria', models.CharField(max_length=2)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Producto - SubCategoria',
                'verbose_name_plural': 'Productos - SubCategorias',
            },
        ),
        migrations.CreateModel(
            name='UnidadMedidaProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unidad_medida_producto', models.CharField(max_length=2)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Producto - Unidad de Medida',
                'verbose_name_plural': 'Productos - Unidades de Medida',
            },
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 19, 23, 1, 3, 971000, tzinfo=utc), help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual.'),
        ),
    ]
