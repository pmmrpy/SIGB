# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0025_auto_20151215_1641'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='precioproducto',
            options={'verbose_name': 'Producto - Precio', 'verbose_name_plural': 'Productos - Precios'},
        ),
        migrations.AlterModelOptions(
            name='recetadetalle',
            options={'verbose_name': 'Receta - Detalle', 'verbose_name_plural': 'Recetas - Detalles'},
        ),
        migrations.AlterModelOptions(
            name='unidadmedida',
            options={'verbose_name': 'Producto - Unidad de Medida', 'verbose_name_plural': 'Productos - Unidades de Medida'},
        ),
        migrations.AlterField(
            model_name='precioproducto',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 18, 20, 27, 48, 119000, tzinfo=utc), help_text=b'Ingrese la fecha y hora en la que se define el precio de venta del producto.'),
        ),
    ]
