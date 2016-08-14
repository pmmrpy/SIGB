# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0087_auto_20160620_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposito',
            name='tipo_deposito',
        ),
        migrations.AlterField(
            model_name='precioproducto',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 20, 17, 4, 4, 167000, tzinfo=utc), help_text=b'Ingrese la fecha y hora en la que se define el precio de venta del producto.'),
        ),
        migrations.DeleteModel(
            name='Deposito',
        ),
    ]
