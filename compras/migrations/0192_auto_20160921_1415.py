# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0191_auto_20160918_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturaproveedor',
            name='numero_factura_compra',
            field=models.CharField(help_text=b'Ingrese el Numero de Factura que acompana la Compra.', max_length=15, verbose_name=b'Numero de Factura Compra'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 22, 18, 15, 11, 508000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordenpago',
            name='proveedor_orden_pago',
            field=models.ForeignKey(verbose_name=b'Proveedor', to='compras.Proveedor', help_text=b'Seleccione el Proveedor para el cual se generara la Orden de Pago.'),
        ),
        migrations.AlterField(
            model_name='ordenpagodetalle',
            name='estado_factura_compra',
            field=models.CharField(blank=True, help_text=b'Indique el Estado de la Factura de la Compra de acuerdo a los pagos aplicados para la misma.', max_length=3, verbose_name=b'Estado de la Factura', choices=[(b'EPP', b'En Plazo de Pago'), (b'FPP', b'Fuera del Plazo de Pago'), (b'PAG', b'Pagada'), (b'CAN', b'Cancelada')]),
        ),
        migrations.AlterField(
            model_name='ordenpagodetalle',
            name='fecha_factura_compra',
            field=models.DateField(default=datetime.date.today, help_text=b'Ingrese la fecha de la Factura.', verbose_name=b'Fecha de la Factura'),
        ),
        migrations.AlterField(
            model_name='ordenpagodetalle',
            name='forma_pago_compra',
            field=models.ForeignKey(verbose_name=b'Forma de Pago', to='bar.FormaPagoCompra', help_text=b'Seleccione la Forma de Pago para esta Factura.'),
        ),
        migrations.AlterField(
            model_name='ordenpagodetalle',
            name='numero_factura_compra',
            field=models.CharField(help_text=b'Ingrese el Numero de Factura que acompana la Compra.', max_length=15, verbose_name=b'Numero de Factura'),
        ),
        migrations.AlterField(
            model_name='ordenpagodetalle',
            name='plazo_factura_compra',
            field=models.PositiveIntegerField(help_text=b'En caso de Credito establecer el plazo de tiempo en dias para el pago.', verbose_name=b'Plazo de Pago'),
        ),
        migrations.AlterField(
            model_name='ordenpagodetalle',
            name='tipo_factura_compra',
            field=models.ForeignKey(verbose_name=b'Tipo de Factura', to='bar.TipoFacturaCompra', help_text=b'Seleccione el Tipo de Factura.'),
        ),
        migrations.AlterField(
            model_name='ordenpagodetalle',
            name='total_factura_compra',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente en funcion al detalle de la Compra.', verbose_name=b'Monto Total de la Factura', max_digits=18, decimal_places=0),
        ),
    ]
