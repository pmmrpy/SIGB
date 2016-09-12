# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0181_auto_20160908_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compradetalle',
            name='unidad_medida_compra',
        ),
        migrations.AlterField(
            model_name='compra',
            name='estado_compra',
            field=models.ForeignKey(default=5, verbose_name=b'Estado Compra', to='bar.OrdenCompraEstado', help_text=b'Se asignan los Estados de la Orden de Compra.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='usuario_registro_compra',
            field=models.ForeignKey(related_name='usuario_registro_compra', default=17, verbose_name=b'Confirmado por?', to='personal.Empleado', help_text=b'Usuario que registro la Compra.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 10, 15, 49, 29, 901000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
    ]
