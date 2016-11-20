# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0078_auto_20161016_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='comanda',
            name='id_pedido_detalle',
            field=models.ForeignKey(default=2, to='ventas.PedidoDetalle'),
        ),
    ]
