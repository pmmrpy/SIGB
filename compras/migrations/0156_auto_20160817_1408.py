# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0155_auto_20160817_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='numero_factura_compra',
            field=models.DecimalField(default=1, help_text=b'Ingrese el Numero de Factura que acompana la Compra.', verbose_name=b'Numero de Factura de la Compra', max_digits=7, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedordetalle',
            name='fecha_movimiento',
            field=models.DateField(default=datetime.datetime(2016, 8, 17, 18, 8, 50, 897000, tzinfo=utc), help_text=b'Ingrese la fecha del Movimiento.', verbose_name=b'Fecha Registro Movimiento'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 18, 18, 8, 50, 901000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='pagoproveedor',
            name='fecha_pago_proveedor',
            field=models.DateField(default=datetime.datetime(2016, 8, 17, 18, 8, 50, 898000, tzinfo=utc), help_text=b'Ingrese la fecha del Pago al Proveedor.', verbose_name=b'Fecha Pago Proveedor'),
        ),
    ]
