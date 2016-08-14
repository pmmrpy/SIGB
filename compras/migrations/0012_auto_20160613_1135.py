# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0011_auto_20160601_1514'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compra',
            options={'verbose_name': 'Confirmacion de Compra', 'verbose_name_plural': 'Confirmaciones de Compras'},
        ),
        migrations.AlterModelOptions(
            name='ordencompra',
            options={'verbose_name': 'Orden de Compra', 'verbose_name_plural': 'Ordenes de Compras'},
        ),
        migrations.AlterModelOptions(
            name='ordencompradetalle',
            options={'verbose_name': 'Orden de Compra - Detalle', 'verbose_name_plural': 'Ordenes de Compras - Detalles'},
        ),
        migrations.AlterModelOptions(
            name='productoproveedor',
            options={'verbose_name': 'Producto por Proveedor', 'verbose_name_plural': 'Productos por Proveedores'},
        ),
        migrations.RenameField(
            model_name='compra',
            old_name='numero_factura',
            new_name='numero_factura_compra',
        ),
        migrations.RenameField(
            model_name='compradetalle',
            old_name='cantidad_producto',
            new_name='cantidad_producto_compra',
        ),
        migrations.RenameField(
            model_name='compradetalle',
            old_name='precio_compra_producto',
            new_name='precio_producto_compra',
        ),
        migrations.RenameField(
            model_name='compradetalle',
            old_name='compra_producto',
            new_name='producto_compra',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='id',
        ),
        migrations.AddField(
            model_name='compra',
            name='compra_id',
            field=models.AutoField(primary_key=True, serialize=False, help_text=b'Este dato se genera automaticamente cada vez que se va a confirmar una Compra.', verbose_name=b'ID de Compra'),
        ),
        migrations.AddField(
            model_name='compra',
            name='fecha_factura_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 13, 15, 35, 17, 459000, tzinfo=utc), help_text=b'Ingrese la fecha de la factura.'),
        ),
        migrations.AddField(
            model_name='compradetalle',
            name='total_producto_compra',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='compra',
            name='estado_compra',
            field=models.ForeignKey(default=1, to='bar.CompraEstado', help_text=b'La Compra solo puede tener 2 estados: CONFIRMADA o CANCELADA.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 13, 15, 35, 17, 459000, tzinfo=utc), help_text=b'La fecha y hora se asignan al momento de guardar los datos de la Compra. No se requiere el ingreso de este dato.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='numero_orden_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Numero de Orden de Compra', to='compras.OrdenCompra', help_text=b'Seleccione el Numero de Orden de Compra para la cual se confirmara la Compra.'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='fecha_linea_credito_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 13, 15, 35, 17, 456000, tzinfo=utc), help_text=b'Ingrese la fecha en la quese registra la Linea deCredito ofrecida por el Proveedor.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='estado_orden_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Estado de la Orden de Compra', to='bar.OrdenCompraEstado', help_text=b'El estado de la Orden de Compra se define de acuerdo a la Fecha de Entrega definida.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 14, 15, 35, 17, 458000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 13, 15, 35, 17, 458000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de la Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='forma_pago_orden_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Forma de Pago', to='bar.FormaPagoCompra', help_text=b'Seleccione la Forma de Pago para esta Orden de Compra.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='total_orden_compra',
            field=models.DecimalField(default=0, verbose_name=b'Total de la Orden de Compra', max_digits=20, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='ordencompradetalle',
            name='cantidad_producto_orden_compra',
            field=models.DecimalField(help_text=b'Ingrese la cantidad a adquirir del producto.', max_digits=10, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='ordencompradetalle',
            name='producto_orden_compra',
            field=models.ForeignKey(related_name='orden_compra_productos', to='compras.ProductoProveedor', help_text=b'Seleccione un producto a ordenar.'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 13, 15, 35, 17, 456000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Proveedor. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
    ]
