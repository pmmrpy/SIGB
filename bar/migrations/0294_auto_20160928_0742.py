# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0293_auto_20160927_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facturaventa',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='timbrado',
            name='empresa',
        ),
        migrations.AlterField(
            model_name='pedidoestado',
            name='pedido_estado',
            field=models.CharField(help_text=b'Ingrese el identificador del Estado del Pedido. (Hasta 3 caracteres)', max_length=3, verbose_name=b'Estado del Pedido', choices=[(b'VIG', b'Vigente'), (b'PRO', b'Procesado'), (b'CAN', b'Cancelado'), (b'ANU', b'Anulada')]),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 9, 28, 7, 42, 26, 634000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
        migrations.AlterField(
            model_name='ventaestado',
            name='venta_estado',
            field=models.CharField(help_text=b'Ingrese el identificador del Estado de la Venta. (Hasta 3 caracteres)', max_length=3, verbose_name=b'Estado de la Venta', choices=[(b'CON', b'Confirmada'), (b'ANU', b'Anulada'), (b'CAN', b'Cancelada'), (b'PEN', b'Pendiente Confirmacion')]),
        ),
    ]
