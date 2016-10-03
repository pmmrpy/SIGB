# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0053_comanda_venta_ventadetalle'),
        ('bar', '0301_auto_20161002_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturaventa',
            name='venta',
            field=models.ForeignKey(default=1, to='ventas.Venta'),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 10, 2, 15, 5, 36, 523000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
    ]
