# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0102_auto_20160619_1901'),
        ('compras', '0020_auto_20160619_1901'),
        ('stock', '0082_auto_20160616_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='subcategoria',
            field=models.ForeignKey(default=1, to='bar.SubCategoriaProducto'),
        ),
        migrations.AlterField(
            model_name='precioproducto',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 19, 23, 1, 4, 14000, tzinfo=utc), help_text=b'Ingrese la fecha y hora en la que se define el precio de venta del producto.'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='unidad_medida',
            field=models.ForeignKey(to='bar.UnidadMedidaProducto'),
        ),
        migrations.DeleteModel(
            name='UnidadMedida',
        ),
    ]
