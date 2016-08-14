# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0042_auto_20160524_1317'),
    ]

    operations = [
        # migrations.AlterField(
            # model_name='compra',
            # name='estado_compra',
            # field=models.ForeignKey(default=b'EPP', to='bar.CompraEstado', help_text=b'El estado de compra se define '),
        # ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 25, 17, 29, 39, 689000, tzinfo=utc), help_text=b'Indique la fecha en la que el proveedor debe entregar el pedido.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 24, 17, 29, 39, 689000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se realiza el pedido.'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='fecha_linea_credito_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 24, 17, 29, 39, 686000, tzinfo=utc), help_text=b'Ingrese la fecha en la quese registra la Linea deCredito ofrecida por el Proveedor.'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 24, 17, 29, 39, 685000, tzinfo=utc), help_text=b'Ingrese la fecha en la que serealiza el alta del Proveedor.'),
        ),
    ]
