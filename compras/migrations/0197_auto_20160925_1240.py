# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0196_auto_20160924_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturaproveedor',
            name='total_pago_factura',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente en funcion a los pagos registrados para la Factura.', verbose_name=b'Monto Total Pagado de la Factura Compra', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedordetalle',
            name='fecha_hora_anulacion',
            field=models.DateTimeField(null=True, verbose_name=b'Fecha/hora Anulacion', blank=True),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 26, 16, 39, 59, 191000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordenpago',
            name='fecha_hora_orden_pago',
            field=models.DateTimeField(help_text=b'La fecha y hora de la Orden de Pago se asignan al momento de guardar los datos del pago. No se requiere el ingreso de este dato.', verbose_name=b'Fecha/hora Orden de Pago', auto_now=True),
        ),
        migrations.AlterField(
            model_name='pagoproveedor',
            name='fecha_hora_anulacion',
            field=models.DateTimeField(null=True, verbose_name=b'Fecha/hora Anulacion', blank=True),
        ),
    ]
