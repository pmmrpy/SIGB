# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0056_remove_pedidodetalle_anulado'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidodetalle',
            name='anulado',
            field=models.BooleanField(default=False, help_text=b'Seleccione esta casilla si desea anular el Producto solicitado.', verbose_name=b'Anular?'),
        ),
        migrations.AlterField(
            model_name='pedidodetalle',
            name='fecha_pedido_detalle',
            field=models.DateTimeField(help_text=b'Registra la fecha y hora en que se realizo el detalle del Pedido, util cuando el cliente pide mas productos.', verbose_name=b'Fecha/hora del Pedido', auto_now_add=True),
        ),
    ]
