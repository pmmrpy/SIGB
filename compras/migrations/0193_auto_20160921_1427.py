# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0192_auto_20160921_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineacreditoproveedordetalle',
            name='numero_comprobante',
            field=models.CharField(help_text=b'Corresponde al Numero de Factura o Numero de Comprobante de Pago del movimiento.', max_length=15, verbose_name=b'Numero Comprobante Movimiento'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 22, 18, 27, 38, 741000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
    ]
