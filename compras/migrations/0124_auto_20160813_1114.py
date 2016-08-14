# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0123_auto_20160813_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineacreditoproveedordetalle',
            name='fecha_movimiento',
            field=models.DateField(default=datetime.datetime(2016, 8, 13, 15, 13, 57, 497000, tzinfo=utc), help_text=b'Ingrese la fecha del Movimiento.', verbose_name=b'Fecha Registro Movimiento'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 14, 15, 13, 57, 502000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 13, 15, 13, 57, 501000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de la Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='pagoproveedor',
            name='fecha_pago_proveedor',
            field=models.DateField(default=datetime.datetime(2016, 8, 13, 15, 13, 57, 499000, tzinfo=utc), help_text=b'Ingrese la fecha del Pago al Proveedor.', verbose_name=b'Fecha Pago Proveedor'),
        ),
    ]
