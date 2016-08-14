# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0044_auto_20160524_1333'),
    ]

    operations = [
        # migrations.RemoveField(
            # model_name='compra',
            # name='estado_compra',
        # ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 25, 17, 38, 53, 442000, tzinfo=utc), help_text=b'Indique la fecha en la que el proveedor debe entregar el pedido.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 24, 17, 38, 53, 442000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se realiza el pedido.'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='fecha_linea_credito_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 24, 17, 38, 53, 439000, tzinfo=utc), help_text=b'Ingrese la fecha en la quese registra la Linea deCredito ofrecida por el Proveedor.'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 24, 17, 38, 53, 438000, tzinfo=utc), help_text=b'Ingrese la fecha en la que serealiza el alta del Proveedor.'),
        ),
    ]
