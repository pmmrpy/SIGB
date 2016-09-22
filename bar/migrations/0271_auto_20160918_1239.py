# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0270_auto_20160911_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordencompraestado',
            name='estado_orden_compra',
            field=models.CharField(max_length=3, verbose_name=b'Estado de la Orden de Compra', choices=[(b'EPP', b'En Proceso Proveedor'), (b'ENT', b'Entregada por el Proveedor'), (b'PEP', b'Pendiente de Entrega por el Proveedor'), (b'CAN', b'Cancelada'), (b'PEN', b'Pendiente Confirmacion')]),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 9, 18, 12, 39, 31, 532000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
    ]
