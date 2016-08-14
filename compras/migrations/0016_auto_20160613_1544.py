# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0015_auto_20160613_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='estado_compra',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='numero_orden_compra',
        ),
        migrations.RemoveField(
            model_name='compradetalle',
            name='compra',
        ),
        migrations.RemoveField(
            model_name='compradetalle',
            name='producto_compra',
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='fecha_linea_credito_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 13, 19, 44, 20, 373000, tzinfo=utc), help_text=b'Ingrese la fecha en la quese registra la Linea deCredito ofrecida por el Proveedor.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='estado_orden_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Estado de la Orden de Compra', to='bar.OrdenCompraEstado', help_text=b'El estado de la Orden de Compra se establece automaticamente de acuerdo a la Fecha de Entrega ingresada.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 14, 19, 44, 20, 374000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 13, 19, 44, 20, 374000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de la Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='forma_pago_orden_compra',
            field=models.ForeignKey(verbose_name=b'Forma de Pago', to='bar.FormaPagoCompra', help_text=b'Seleccione la Forma de Pago para esta Orden de Compra.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='proveedor_orden_compra',
            field=models.ForeignKey(verbose_name=b'Proveedor', to='compras.Proveedor', help_text=b'Seleccione el Proveedor al cual se le realizara la Orden de Compra.'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 13, 19, 44, 20, 372000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Proveedor. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
        migrations.DeleteModel(
            name='Compra',
        ),
        migrations.DeleteModel(
            name='CompraDetalle',
        ),
    ]
