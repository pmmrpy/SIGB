# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0145_auto_20160816_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturaproveedor',
            name='estado_factura_compra',
            field=models.CharField(default=b'PEN', help_text=b'Indique el Estado de la Factura de la Compra de acuerdo a los pagos aplicados para la misma.', max_length=3, verbose_name=b'Estado de la Factura de la Compra', choices=[(b'PEN', b'Pendiente'), (b'PAG', b'Pagada'), (b'CAN', b'Cancelada')]),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedordetalle',
            name='fecha_movimiento',
            field=models.DateField(default=datetime.datetime(2016, 8, 16, 12, 4, 53, 454000, tzinfo=utc), help_text=b'Ingrese la fecha del Movimiento.', verbose_name=b'Fecha Registro Movimiento'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 17, 12, 4, 53, 460000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='pagoproveedor',
            name='fecha_pago_proveedor',
            field=models.DateField(default=datetime.datetime(2016, 8, 16, 12, 4, 53, 456000, tzinfo=utc), help_text=b'Ingrese la fecha del Pago al Proveedor.', verbose_name=b'Fecha Pago Proveedor'),
        ),
    ]
