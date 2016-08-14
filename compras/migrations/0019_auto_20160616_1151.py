# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0018_auto_20160613_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fecha_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 16, 15, 51, 52, 900000, tzinfo=utc), help_text=b'La fecha y hora se asignan al momento de guardar los datos de la Compra. No se requiere el ingreso de este dato.', verbose_name=b'Fecha y hora de la Compra'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_factura_compra',
            field=models.DateField(default=datetime.datetime(2016, 6, 16, 15, 51, 52, 900000, tzinfo=utc), help_text=b'Ingrese la fecha de la factura.', verbose_name=b'Fecha de la Factura de la Compra'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='fecha_linea_credito_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 16, 15, 51, 52, 895000, tzinfo=utc), help_text=b'Ingrese la fecha en la quese registra la Linea deCredito ofrecida por el Proveedor.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 17, 15, 51, 52, 898000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 16, 15, 51, 52, 898000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de la Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='total_orden_compra',
            field=models.DecimalField(default=0, verbose_name=b'Total de la Orden de Compra', max_digits=20, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='ordencompradetalle',
            name='cantidad_producto_orden_compra',
            field=models.DecimalField(help_text=b'Ingrese la cantidad a adquirir del producto.', verbose_name=b'Cantidad del Producto', max_digits=10, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='ordencompradetalle',
            name='precio_producto_orden_compra',
            field=models.DecimalField(help_text=b'Ingrese el precio de compra del producto definido por el proveedor.', verbose_name=b'Precio del Producto', max_digits=20, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='ordencompradetalle',
            name='producto_orden_compra',
            field=models.ForeignKey(related_name='orden_compra_productos', verbose_name=b'Producto', to='compras.ProductoProveedor', help_text=b'Seleccione un producto a ordenar.'),
        ),
        migrations.AlterField(
            model_name='ordencompradetalle',
            name='total_producto_orden_compra',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente tomando el Precio del Producto por la Cantidad del Producto.', verbose_name=b'Total del Producto', max_digits=20, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 16, 15, 51, 52, 895000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Proveedor. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
    ]
