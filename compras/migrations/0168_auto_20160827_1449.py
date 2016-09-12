# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0167_auto_20160827_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineacreditoproveedor',
            name='disponible_linea_credito_proveedor',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente como la diferencia entre el Monto de la Linea de Credito y el Monto Utilizado de la Linea de Credito.', verbose_name=b'Monto Disponible Linea de Credito', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedordetalle',
            name='fecha_movimiento',
            field=models.DateField(default=datetime.datetime(2016, 8, 27, 18, 49, 42, 384000, tzinfo=utc), help_text=b'Ingrese la fecha del Movimiento.', verbose_name=b'Fecha Registro Movimiento'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 28, 18, 49, 42, 389000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='pagoproveedor',
            name='fecha_pago_proveedor',
            field=models.DateField(default=datetime.datetime(2016, 8, 27, 18, 49, 42, 386000, tzinfo=utc), help_text=b'Ingrese la fecha del Pago al Proveedor.', verbose_name=b'Fecha Pago Proveedor'),
        ),
    ]
