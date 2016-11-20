# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0262_auto_20161024_1028'),
        ('bar', '0344_auto_20161023_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturaventa',
            name='empresa',
            field=models.ForeignKey(default=9, to='compras.Empresa'),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='utilizada_por_numero_pedido',
            field=models.PositiveIntegerField(null=True, verbose_name=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 10, 24, 10, 28, 26, 204000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
    ]
