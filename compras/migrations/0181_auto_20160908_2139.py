# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0180_auto_20160908_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='numero_factura_compra',
            field=models.DecimalField(default=1, help_text=b'Ingrese el Numero de Factura que acompana la Compra.', verbose_name=b'Numero de Factura Compra', max_digits=13, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='compra',
            name='usuario_registro_compra',
            field=models.ForeignKey(related_name='usuario_registro_compra', default=1, verbose_name=b'Confirmado por?', to='personal.Empleado', help_text=b'Usuario que registro la Compra.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 10, 1, 39, 4, 244000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
    ]
