# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0023_auto_20160731_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fecha_pedido',
            field=models.DateTimeField(help_text=b'La fecha y hora del Pedido se asignara automaticamente una vez que sea guardado.', verbose_name=b'Fecha/Hora del Pedido', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='pedidodetalle',
            name='fecha_pedido_detalle',
            field=models.DateTimeField(help_text=b'Registra la fecha y hora en que se realizo el detalle del Pedido, util cuando el cliente pide mas productos.', verbose_name=b'Fecha/hora del detalle del Pedido', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha_venta',
            field=models.DateTimeField(help_text=b'Registra la fecha y hora en la que se confirmo la Venta.', verbose_name=b'Fecha/hora de la Venta', auto_now_add=True),
        ),
    ]
