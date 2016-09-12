# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0147_auto_20160816_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(default=9, to='compras.Proveedor'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='tipo_factura_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Tipo de Factura', to='bar.TipoFacturaCompra', help_text=b'Seleccione el Tipo de Factura para la Compra.'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedordetalle',
            name='fecha_movimiento',
            field=models.DateField(default=datetime.datetime(2016, 8, 16, 17, 18, 32, 503000, tzinfo=utc), help_text=b'Ingrese la fecha del Movimiento.', verbose_name=b'Fecha Registro Movimiento'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 17, 17, 18, 32, 510000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='pagoproveedor',
            name='fecha_pago_proveedor',
            field=models.DateField(default=datetime.datetime(2016, 8, 16, 17, 18, 32, 506000, tzinfo=utc), help_text=b'Ingrese la fecha del Pago al Proveedor.', verbose_name=b'Fecha Pago Proveedor'),
        ),
    ]
