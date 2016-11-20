# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0315_auto_20161008_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numerofacturaventa',
            name='fecha_hora_uso',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='numerofacturaventa',
            name='venta_asociada',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 10, 8, 19, 22, 52, 543000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
    ]
