# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0079_comanda_id_pedido_detalle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='id_pedido_detalle',
            field=models.ForeignKey(to='ventas.PedidoDetalle'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='estado_venta',
            field=models.ForeignKey(verbose_name=b'Estado Venta', to='bar.VentaEstado', help_text=b'El estado de la Venta se establece automaticamente una vez que es confirmada la misma.'),
        ),
    ]
