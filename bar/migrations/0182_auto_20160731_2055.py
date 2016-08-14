# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0181_auto_20160731_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(help_text=b'Registra la fecha y hora en la que se definio la Cotizacion. Corresponde a la fecha y hora actual.', verbose_name=b'Fecha de Cotizacion', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_autorizacion_timbrado',
            field=models.DateField(default=datetime.datetime(2016, 7, 31, 20, 55, 3, 220000), help_text=b'Ingrese la Fecha de Autorizacion del Timbrado', verbose_name=b'Fecha de Autorizacion del Timbrado'),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 7, 31, 20, 55, 3, 220000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
    ]
