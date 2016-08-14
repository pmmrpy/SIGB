# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0173_auto_20160726_2040'),
        ('ventas', '0014_auto_20160722_1515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aperturacaja',
            options={'verbose_name': 'Apertura de Caja', 'verbose_name_plural': 'Apertura de Cajas'},
        ),
        migrations.AlterModelOptions(
            name='cocina',
            options={'verbose_name': 'Cocina', 'verbose_name_plural': 'Cocina'},
        ),
        migrations.AddField(
            model_name='venta',
            name='numero_factura_venta',
            field=models.ForeignKey(default=1, verbose_name=b'Numero de Factura de la Venta', to='bar.Facturas', help_text=b''),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 27, 0, 39, 58, 173000, tzinfo=utc), help_text=b'', verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='pedidodetalle',
            name='fecha_pedido_detalle',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 27, 0, 39, 58, 174000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha_venta',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 27, 0, 39, 58, 175000, tzinfo=utc)),
        ),
    ]
