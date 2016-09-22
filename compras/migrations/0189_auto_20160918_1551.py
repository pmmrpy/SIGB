# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0188_auto_20160918_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturaproveedor',
            name='numero_orden_pago',
            field=models.OneToOneField(null=True, to='compras.OrdenPago'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 19, 19, 51, 5, 176000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
    ]
