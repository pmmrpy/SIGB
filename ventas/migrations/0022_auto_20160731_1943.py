# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0021_auto_20160731_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 31, 23, 43, 19, 164000, tzinfo=utc), help_text=b'La fecha y hora del Pedido se asignara automaticamente una vez que sea guardado.', verbose_name=b'Fecha/Hora del Pedido'),
        ),
        migrations.AlterField(
            model_name='pedidodetalle',
            name='fecha_pedido_detalle',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 31, 23, 43, 19, 165000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha_venta',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 31, 23, 43, 19, 165000, tzinfo=utc)),
        ),
    ]
