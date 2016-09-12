# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0135_auto_20160814_2254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compra',
            options={'verbose_name': 'Compra - Confirmacion', 'verbose_name_plural': 'Compras - Confirmaciones'},
        ),
        migrations.AlterModelOptions(
            name='compradetalle',
            options={'verbose_name': 'Compra - Detalle de Confirmacion', 'verbose_name_plural': 'Compras - Detalles de Confirmaciones'},
        ),
        migrations.AlterModelOptions(
            name='lineacreditoproveedor',
            options={'verbose_name': 'Proveedor - Linea de Credito', 'verbose_name_plural': 'Proveedores - Lineas de Credito'},
        ),
        migrations.AlterModelOptions(
            name='ordencompra',
            options={'verbose_name': 'Compra - Orden', 'verbose_name_plural': 'Compras - Ordenes'},
        ),
        migrations.AlterModelOptions(
            name='ordencompradetalle',
            options={'verbose_name': 'Compra - Detalle de Orden', 'verbose_name_plural': 'Compras - Detalles de Ordenes'},
        ),
        migrations.AlterModelOptions(
            name='productoproveedor',
            options={'verbose_name': 'Proveedor - Producto', 'verbose_name_plural': 'Proveedores - Productos'},
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_factura_compra',
            field=models.DateField(default=datetime.date(2016, 8, 15), help_text=b'Ingrese la fecha de la factura.', verbose_name=b'Fecha de la Factura de la Compra'),
        ),
        migrations.AlterField(
            model_name='facturaproveedor',
            name='fecha_factura_compra',
            field=models.DateField(default=datetime.date(2016, 8, 15), help_text=b'Ingrese la fecha de la Factura.', verbose_name=b'Fecha de la Factura de la Compra'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedordetalle',
            name='fecha_movimiento',
            field=models.DateField(default=datetime.datetime(2016, 8, 15, 14, 56, 11, 439000, tzinfo=utc), help_text=b'Ingrese la fecha del Movimiento.', verbose_name=b'Fecha Registro Movimiento'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 16, 14, 56, 11, 446000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 15, 14, 56, 11, 446000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de la Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='pagoproveedor',
            name='fecha_pago_proveedor',
            field=models.DateField(default=datetime.datetime(2016, 8, 15, 14, 56, 11, 441000, tzinfo=utc), help_text=b'Ingrese la fecha del Pago al Proveedor.', verbose_name=b'Fecha Pago Proveedor'),
        ),
    ]
