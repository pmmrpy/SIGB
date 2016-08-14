# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0199_auto_20160730_1456'),
        ('compras', '0092_auto_20160730_1456'),
        ('ventas', '0016_auto_20160729_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='reserva',
            field=models.ForeignKey(default=1, to='clientes.Reserva'),
        ),
        migrations.AddField(
            model_name='venta',
            name='empresa',
            field=models.ForeignKey(default=1, to='compras.Empresa'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 30, 18, 56, 4, 161000, tzinfo=utc), help_text=b'', verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='pedidodetalle',
            name='fecha_pedido_detalle',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 30, 18, 56, 4, 162000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha_venta',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 30, 18, 56, 4, 163000, tzinfo=utc)),
        ),
    ]
