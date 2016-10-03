# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0297_auto_20160930_1145'),
        ('compras', '0213_auto_20160930_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturaproveedor',
            name='estado_factura_compra',
            field=models.ForeignKey(default=1, blank=True, to='bar.FacturaProveedorEstado', help_text=b'Indique el Estado de la Factura de la Compra de acuerdo a los pagos aplicados para la misma.', verbose_name=b'Estado de la Factura'),
        ),
        migrations.AddField(
            model_name='ordenpago',
            name='estado_orden_pago',
            field=models.ForeignKey(default=1, blank=True, to='bar.OrdenPagoEstado', help_text=b'Se asigna automaticamente de acuerdo a la accion que se realice con la Orden de Pago.', verbose_name=b'Estado Orden de Pago'),
        ),
        migrations.AddField(
            model_name='ordenpagodetalle',
            name='estado_factura_compra',
            field=models.ForeignKey(default=1, blank=True, to='bar.FacturaProveedorEstado', help_text=b'Indique el Estado de la Factura de la Compra de acuerdo a los pagos aplicados para la misma.', verbose_name=b'Estado de la Factura'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 1, 15, 45, 4, 737000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
    ]
