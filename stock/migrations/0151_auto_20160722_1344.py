# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0013_auto_20160722_1344'),
        ('stock', '0150_auto_20160722_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='precioproducto',
            name='producto',
        ),
        migrations.AlterField(
            model_name='stock',
            name='fecha_hora_registro_stock',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 22, 17, 44, 45, 28000, tzinfo=utc), help_text=b'Fecha y hora de registro en el Stock.', verbose_name=b'Fecha y hora de registro'),
        ),
        migrations.DeleteModel(
            name='PrecioProducto',
        ),
    ]
