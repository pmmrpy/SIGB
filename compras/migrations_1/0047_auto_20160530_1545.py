# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0054_auto_20160530_1545'),
        ('compras', '0046_auto_20160528_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordencompradetalle',
            old_name='cantidad_producto',
            new_name='cantidad_producto_orden_compra',
        ),
        migrations.RenameField(
            model_name='ordencompradetalle',
            old_name='precio_orden_compra_producto',
            new_name='precio_producto_orden_compra',
        ),
        migrations.RenameField(
            model_name='ordencompradetalle',
            old_name='orden_compra_producto',
            new_name='producto_orden_compra',
        ),
        migrations.RemoveField(
            model_name='ordencompra',
            name='fecha_entrega',
        ),
        migrations.RemoveField(
            model_name='ordencompra',
            name='fecha_pedido',
        ),
        migrations.RemoveField(
            model_name='ordencompra',
            name='forma_pago',
        ),
        migrations.RemoveField(
            model_name='ordencompra',
            name='proveedor_compra',
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='estado_orden_compra',
            field=models.ForeignKey(default=1, to='bar.OrdenCompraEstado', help_text=b'El estado de la Orden de Compra se define de acuerdo a la Fecha de Entrega definida.'),
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 31, 19, 45, 19, 477000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.'),
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 30, 19, 45, 19, 477000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.'),
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='forma_pago_orden_compra',
            field=models.ForeignKey(default=1, to='bar.FormaPagoCompra', help_text=b'Seleccione la Forma de Pago para esta Orden de Compra.'),
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='proveedor_orden_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Proveedor', to='compras.Proveedor', help_text=b'Seleccione el Proveedor al cual se le realizara la Orden de Compra.'),
        ),
        migrations.AddField(
            model_name='ordencompradetalle',
            name='total_producto_orden_compra',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='compra',
            name='estado_compra',
            field=models.ForeignKey(default=1, to='bar.CompraEstado', help_text=b'El estado de compra se define de acuerdo a la Fecha de Entrega definida en la Orden de Compra.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 30, 19, 45, 19, 479000, tzinfo=utc), help_text=b'La fecha y hora se asignan al momento de guardar los datos de la Compra. No se requiere el ingreso de este dato.'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='fecha_linea_credito_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 30, 19, 45, 19, 474000, tzinfo=utc), help_text=b'Ingrese la fecha en la quese registra la Linea deCredito ofrecida por el Proveedor.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='numero_orden_compra',
            field=models.CharField(help_text=b'Este dato se genera automaticamente cada vez que se va crear una Orden de Compra.', unique=True, max_length=6, verbose_name=b'Numero de Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 30, 19, 45, 19, 474000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Proveedor. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
    ]
