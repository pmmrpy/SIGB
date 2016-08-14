# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0196_auto_20160810_1136'),
        ('compras', '0112_auto_20160810_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='tipo_factura_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Tipo de Factura', to='bar.TipoFacturaCompra', help_text=b'Seleccione el Tipo de Factura para la Compra.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 11, 15, 36, 39, 222000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 10, 15, 36, 39, 222000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de la Orden de Compra'),
        ),
    ]