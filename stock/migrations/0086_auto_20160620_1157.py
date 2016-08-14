# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0085_auto_20160620_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precioproducto',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 20, 15, 56, 59, 928000, tzinfo=utc), help_text=b'Ingrese la fecha y hora en la que se define el precio de venta del producto.'),
        ),
    ]