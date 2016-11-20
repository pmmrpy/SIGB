# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0321_auto_20161116_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='tipo_factura_compra',
            field=models.ForeignKey(verbose_name=b'Tipo de Factura', blank=True, to='bar.TipoFacturaCompra', help_text=b'Seleccione el Tipo de Factura para la Compra.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 19, 19, 41, 2, 152000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
    ]
