# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0174_auto_20160729_1513'),
        ('ventas', '0015_auto_20160726_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='empresa',
        ),
        migrations.AddField(
            model_name='venta',
            name='caja',
            field=models.ForeignKey(default=1, to='bar.Caja'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 29, 19, 13, 50, 391000, tzinfo=utc), help_text=b'', verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='pedidodetalle',
            name='fecha_pedido_detalle',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 29, 19, 13, 50, 393000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha_venta',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 29, 19, 13, 50, 394000, tzinfo=utc)),
        ),
    ]
