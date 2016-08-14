# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0032_auto_20160528_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precioproducto',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 28, 15, 41, 39, 269000, tzinfo=utc), help_text=b'Ingrese la fecha y hora en la que se define el precio de venta del producto.'),
        ),
    ]
