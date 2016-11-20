# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0336_auto_20161018_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesa',
            name='utilizada_por_numero_pedido',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Utilizada por Numero Pedido', blank=True),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 10, 22, 12, 31, 53, 935000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
    ]
