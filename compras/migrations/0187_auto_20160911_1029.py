# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0186_auto_20160910_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='estado_compra',
            field=models.ForeignKey(verbose_name=b'Estado Compra', to='bar.OrdenCompraEstado', help_text=b'Se asignan los Estados de la Orden de Compra.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='numero_factura_compra',
            field=models.DecimalField(help_text=b'Ingrese el Numero de Factura que acompana la Compra.', verbose_name=b'Numero de Factura Compra', max_digits=13, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 12, 14, 28, 57, 6000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
    ]
