# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_auto_20151025_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precioproducto',
            name='activo',
            field=models.BooleanField(default=True, help_text=b'Indique si este precio es el que se encuentra activo actualmente. El producto puede tener un unico precio activo.'),
        ),
        migrations.AlterField(
            model_name='precioproducto',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 9, 0, 25, 8, 416000, tzinfo=utc), help_text=b'Ingrese la fecha y hora en la que se define el precio de venta del producto.'),
        ),
        migrations.AlterField(
            model_name='precioproducto',
            name='precio_venta',
            field=models.DecimalField(help_text=b'Ingrese el precio de venta del producto.', max_digits=20, decimal_places=2),
        ),
    ]
