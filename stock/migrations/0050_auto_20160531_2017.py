# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0049_auto_20160531_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precioproducto',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 1, 0, 17, 49, 706000, tzinfo=utc), help_text=b'Ingrese la fecha y hora en la que se define el precio de venta del producto.'),
        ),
    ]
