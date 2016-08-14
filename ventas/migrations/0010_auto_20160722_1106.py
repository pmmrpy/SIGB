# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0009_auto_20160722_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 22, 15, 6, 31, 759000, tzinfo=utc), help_text=b'', verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='pedidodetalle',
            name='fecha_pedido_detalle',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 22, 15, 6, 31, 760000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha_venta',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 22, 15, 6, 31, 761000, tzinfo=utc)),
        ),
    ]
