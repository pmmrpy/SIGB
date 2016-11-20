# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0379_auto_20161102_1438'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='numerofacturaventa',
            options={'verbose_name': 'Venta - Numero de Factura', 'verbose_name_plural': 'Ventas - Numeros de Facturas'},
        ),
        migrations.AlterField(
            model_name='pedidoestado',
            name='pedido_estado',
            field=models.CharField(help_text=b'Ingrese el identificador del Estado del Pedido. (Hasta 3 caracteres)', max_length=3, verbose_name=b'Estado del Pedido', choices=[(b'VIG', b'Vigente'), (b'PRO', b'Procesado'), (b'CAN', b'Cancelado'), (b'ANU', b'Anulada'), (b'PEN', b'Pendiente Confirmacion')]),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 11, 5, 22, 38, 4, 215000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
        migrations.AlterField(
            model_name='ventaestado',
            name='venta_estado',
            field=models.CharField(help_text=b'Ingrese el identificador del Estado de la Venta. (Hasta 3 caracteres)', max_length=3, verbose_name=b'Estado de la Venta', choices=[(b'PRO', b'Procesado'), (b'ANU', b'Anulada'), (b'PEN', b'Pendiente Confirmacion')]),
        ),
    ]
