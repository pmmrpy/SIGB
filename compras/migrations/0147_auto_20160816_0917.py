# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0146_auto_20160816_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(default=2, to='compras.Proveedor'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='tipo_factura_compra',
            field=models.ForeignKey(verbose_name=b'Tipo de Factura', to='bar.TipoFacturaCompra', help_text=b'Seleccione el Tipo de Factura para la Compra.'),
        ),
        migrations.AlterField(
            model_name='facturaproveedor',
            name='estado_factura_compra',
            field=models.CharField(default=b'PEN', help_text=b'Indique el Estado de la Factura de la Compra de acuerdo a los pagos aplicados para la misma.', max_length=3, verbose_name=b'Estado de la Factura Compra', choices=[(b'PEN', b'Pendiente'), (b'PAG', b'Pagada'), (b'CAN', b'Cancelada')]),
        ),
        migrations.AlterField(
            model_name='facturaproveedor',
            name='fecha_factura_compra',
            field=models.DateField(default=datetime.date(2016, 8, 16), help_text=b'Ingrese la fecha de la Factura.', verbose_name=b'Fecha de la Factura Compra'),
        ),
        migrations.AlterField(
            model_name='facturaproveedor',
            name='numero_factura_compra',
            field=models.IntegerField(help_text=b'Ingrese el Numero de Factura que acompana la Compra.', verbose_name=b'Numero de Factura Compra'),
        ),
        migrations.AlterField(
            model_name='facturaproveedor',
            name='total_factura_compra',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente en funcion al detalle de la Compra.', verbose_name=b'Monto Total de la Factura Compra', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='facturaproveedor',
            name='total_pago_factura',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente en funcion a los pagos registrados para la Factura.', verbose_name=b'Total Pagado de la Factura Compra', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedordetalle',
            name='fecha_movimiento',
            field=models.DateField(default=datetime.datetime(2016, 8, 16, 13, 17, 13, 501000, tzinfo=utc), help_text=b'Ingrese la fecha del Movimiento.', verbose_name=b'Fecha Registro Movimiento'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 17, 13, 17, 13, 506000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='pagoproveedor',
            name='fecha_pago_proveedor',
            field=models.DateField(default=datetime.datetime(2016, 8, 16, 13, 17, 13, 502000, tzinfo=utc), help_text=b'Ingrese la fecha del Pago al Proveedor.', verbose_name=b'Fecha Pago Proveedor'),
        ),
    ]
