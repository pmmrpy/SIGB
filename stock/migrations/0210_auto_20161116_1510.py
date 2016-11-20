# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0209_auto_20161116_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('insumo', models.CharField(help_text=b'Ingrese el nombre o descripcion del Insumo.', max_length=200, verbose_name=b'Nombre del Insumo')),
                ('costo_promedio', models.DecimalField(default=0, help_text=b'Promedio de los Precios de Compra de los Productos integrantes.', verbose_name=b'Costo Promedio', max_digits=18, decimal_places=0)),
            ],
            options={
                'verbose_name': 'Insumo',
                'verbose_name_plural': 'Insumos',
            },
        ),
        # migrations.AlterField(
        #     model_name='producto',
        #     name='producto',
        #     field=models.CharField(help_text=b'Ingrese el nombre o descripcion del Producto.', max_length=200, verbose_name=b'Nombre del Producto'),
        # ),
    ]
