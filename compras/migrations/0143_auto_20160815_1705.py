# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0142_auto_20160815_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordencompra',
            name='fecha_ultima_modificacion_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 15, 21, 5, 26, 623000, tzinfo=utc), help_text=b'Registra la fecha/hora de ultima modificacion de la Orden de Compra.', verbose_name=b'Fecha/hora Ult. Modif.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_compra',
            field=models.DateTimeField(help_text=b'La fecha y hora se asignan al momento de guardar los datos de la Compra. No se requiere el ingreso de este dato.', verbose_name=b'Fecha y hora de la Compra', auto_now=True),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedordetalle',
            name='fecha_movimiento',
            field=models.DateField(default=datetime.datetime(2016, 8, 15, 21, 5, 26, 618000, tzinfo=utc), help_text=b'Ingrese la fecha del Movimiento.', verbose_name=b'Fecha Registro Movimiento'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='estado_orden_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Estado Orden de Compra', to='bar.OrdenCompraEstado', help_text=b'El estado de la Orden de Compra se establece automaticamente de acuerdo a la Fecha de Entrega ingresada.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 16, 21, 5, 26, 623000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.', verbose_name=b'Fecha/hora Registro', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='numero_orden_compra',
            field=models.AutoField(help_text=b'Este dato se genera automaticamente cada vez que se va crear una Orden de Compra.', serialize=False, verbose_name=b'Numero Orden de Compra', primary_key=True),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='total_orden_compra',
            field=models.DecimalField(default=0, verbose_name=b'Total Orden de Compra', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='pagoproveedor',
            name='fecha_pago_proveedor',
            field=models.DateField(default=datetime.datetime(2016, 8, 15, 21, 5, 26, 620000, tzinfo=utc), help_text=b'Ingrese la fecha del Pago al Proveedor.', verbose_name=b'Fecha Pago Proveedor'),
        ),
    ]
