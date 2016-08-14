# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0044_auto_20160623_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='estado_compra',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='ordencompra_ptr',
        ),
        migrations.RemoveField(
            model_name='compradetalle',
            name='compra',
        ),
        migrations.RemoveField(
            model_name='compradetalle',
            name='ordencompradetalle_ptr',
        ),
        migrations.RemoveField(
            model_name='ordencompra',
            name='polymorphic_ctype',
        ),
        migrations.RemoveField(
            model_name='ordencompradetalle',
            name='polymorphic_ctype',
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='fecha_linea_credito_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 23, 18, 21, 21, 939000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se registra la Linea de Credito ofrecida por el Proveedor.', verbose_name=b'Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 24, 18, 21, 21, 942000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 23, 18, 21, 21, 942000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de la Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 23, 18, 21, 21, 938000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Proveedor. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
        migrations.DeleteModel(
            name='Compra',
        ),
        migrations.DeleteModel(
            name='CompraDetalle',
        ),
    ]
