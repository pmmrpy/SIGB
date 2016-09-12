# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.validators
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0179_auto_20160907_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='estado_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Estado Compra', to='bar.OrdenCompraEstado', help_text=b'Se asignan los Estados de la Orden de Compra.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='numero_factura_compra',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=13, validators=[django.core.validators.RegexValidator(b'^999-999-9999999$', b'Ingrese el Numero de Factura en el formato "999-999-9999999".')], help_text=b'Ingrese el Numero de Factura que acompana la Compra.', verbose_name=b'Numero de Factura Compra'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 10, 0, 29, 41, 558000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='usuario_registro_orden_compra',
            field=models.ForeignKey(related_name='usuario_registro', verbose_name=b'Preparado por?', to='personal.Empleado', help_text=b'Usuario que registro la Orden de Compra.'),
        ),
        migrations.AlterField(
            model_name='ordencompradetalle',
            name='precio_producto_orden_compra',
            field=models.DecimalField(help_text=b'Ingrese el precio de compra del producto definido por el proveedor.', verbose_name=b'Precio Compra del Producto', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='pagoproveedor',
            name='factura_proveedor',
            field=models.ForeignKey(verbose_name=b'Factura Proveedor', to='compras.FacturaProveedor', help_text=b'Seleccione la Factura a la cual se aplicara el Pago.'),
        ),
        migrations.AlterField(
            model_name='pagoproveedor',
            name='monto_pago_proveedor',
            field=models.DecimalField(help_text=b'Ingrese el monto abonado al Proveedor.', verbose_name=b'Monto de Pago al Proveedor', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='pagoproveedor',
            name='numero_comprobante_pago',
            field=models.IntegerField(help_text=b'Ingrese el Numero del Comprobante de Pago. El comprobante puede ser una Nota de Credito que anula o cancela la factura de la Compra en caso de que la misma se haya devuelto o cancelado.', verbose_name=b'Numero de Comprobante de Pago'),
        ),
    ]
