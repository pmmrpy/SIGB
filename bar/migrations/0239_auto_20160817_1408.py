# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0238_auto_20160817_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='caja',
            name='marca',
            field=models.CharField(default=b'PC Standard', help_text=b'Ingrese la marca de la Caja.', max_length=50, verbose_name=b'Marca'),
        ),
        migrations.AddField(
            model_name='caja',
            name='modelo_fabricacion',
            field=models.CharField(default=b'PC Standard Proc. Intel - 4 GBs de RAM', help_text=b'Ingrese el modelo de fabricacion de la Caja.', max_length=100, verbose_name=b'Modelo de Fabricacion'),
        ),
        migrations.AddField(
            model_name='caja',
            name='numero_serie',
            field=models.CharField(default=b'1234567890', help_text=b'Ingrese el numero de serie de la Caja.', max_length=20, verbose_name=b'Numero de Serie'),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_autorizacion_timbrado',
            field=models.DateField(default=datetime.datetime(2016, 8, 17, 14, 8, 50, 877000), help_text=b'Ingrese la Fecha de Autorizacion del Timbrado', verbose_name=b'Fecha de Autorizacion del Timbrado'),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 8, 17, 14, 8, 50, 877000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
    ]
