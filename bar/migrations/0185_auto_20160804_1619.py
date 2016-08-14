# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0184_auto_20160803_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidoestado',
            name='pedido_estado',
            field=models.CharField(help_text=b'Ingrese el identificador del Estado del Pedido. (Hasta 3 caracteres)', max_length=3, verbose_name=b'Estado del Pedido', choices=[(b'VIG', b'Vigente'), (b'PRO', b'Procesado'), (b'CAN', b'Cancelado')]),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_autorizacion_timbrado',
            field=models.DateField(default=datetime.datetime(2016, 8, 4, 16, 19, 24, 764000), help_text=b'Ingrese la Fecha de Autorizacion del Timbrado', verbose_name=b'Fecha de Autorizacion del Timbrado'),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 8, 4, 16, 19, 24, 764000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
    ]
