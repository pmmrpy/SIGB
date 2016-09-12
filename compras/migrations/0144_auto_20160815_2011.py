# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0143_auto_20160815_1705'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compra',
            options={'verbose_name': 'Confirmacion de Orden de Compra', 'verbose_name_plural': 'Compras - Confirmaciones de Ordenes'},
        ),
        migrations.AlterModelOptions(
            name='compradetalle',
            options={'verbose_name': 'Detalle de Confirmacion de Orden de Compra', 'verbose_name_plural': 'Compras - Detalles de Confirmaciones de Ordenes'},
        ),
        migrations.AlterModelOptions(
            name='facturaproveedor',
            options={'verbose_name': 'Factura/Pago Proveedor', 'verbose_name_plural': 'Proveedores - Facturas/Pagos'},
        ),
        migrations.AlterModelOptions(
            name='lineacreditoproveedor',
            options={'verbose_name': 'Linea de Credito Proveedor', 'verbose_name_plural': 'Proveedores - Lineas de Credito'},
        ),
        migrations.AlterModelOptions(
            name='lineacreditoproveedordetalle',
            options={'verbose_name': 'Detalle Linea de Credito con Proveedor', 'verbose_name_plural': 'Lineas de Credito con Proveedores - Detalles'},
        ),
        migrations.AlterModelOptions(
            name='ordencompra',
            options={'verbose_name': 'Orden de Compra', 'verbose_name_plural': 'Compras - Ordenes'},
        ),
        migrations.AlterModelOptions(
            name='ordencompradetalle',
            options={'verbose_name': 'Detalle de Orden de Compra', 'verbose_name_plural': 'Compras - Detalles de Ordenes'},
        ),
        migrations.AlterModelOptions(
            name='proveedortelefono',
            options={'verbose_name': 'Telefono del Proveedor', 'verbose_name_plural': 'Proveedores - Telefonos'},
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedordetalle',
            name='fecha_movimiento',
            field=models.DateField(default=datetime.datetime(2016, 8, 16, 0, 11, 36, 527000, tzinfo=utc), help_text=b'Ingrese la fecha del Movimiento.', verbose_name=b'Fecha Registro Movimiento'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 17, 0, 11, 36, 531000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.', verbose_name=b'Fecha/hora Orden de Compra', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_ultima_modificacion_orden_compra',
            field=models.DateTimeField(help_text=b'Registra la fecha/hora de ultima modificacion de la Orden de Compra.', verbose_name=b'Fecha/hora Ult. Modif.', auto_now=True),
        ),
        migrations.AlterField(
            model_name='pagoproveedor',
            name='fecha_pago_proveedor',
            field=models.DateField(default=datetime.datetime(2016, 8, 16, 0, 11, 36, 528000, tzinfo=utc), help_text=b'Ingrese la fecha del Pago al Proveedor.', verbose_name=b'Fecha Pago Proveedor'),
        ),
    ]
