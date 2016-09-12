# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0260_auto_20160817_1459'),
        ('compras', '0156_auto_20160817_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='usuario_registro_compra',
            field=models.ForeignKey(related_name='usuario_registro_compra', default=1, verbose_name=b'Confirmado por?', to_field=b'usuario', to='personal.Empleado', help_text=b'Usuario que registro la Compra.'),
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='usuario_registro_orden_compra',
            field=models.ForeignKey(related_name='usuario_registro_orden_compra', default=1, verbose_name=b'Preparado por?', to_field=b'usuario', to='personal.Empleado', help_text=b'Usuario que registro la Orden de Compra.'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedordetalle',
            name='fecha_movimiento',
            field=models.DateField(default=datetime.datetime(2016, 8, 17, 18, 59, 26, 219000, tzinfo=utc), help_text=b'Ingrese la fecha del Movimiento.', verbose_name=b'Fecha Registro Movimiento'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 18, 18, 59, 26, 224000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='pagoproveedor',
            name='fecha_pago_proveedor',
            field=models.DateField(default=datetime.datetime(2016, 8, 17, 18, 59, 26, 221000, tzinfo=utc), help_text=b'Ingrese la fecha del Pago al Proveedor.', verbose_name=b'Fecha Pago Proveedor'),
        ),
    ]
