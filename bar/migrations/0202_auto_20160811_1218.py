# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0201_auto_20160811_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_autorizacion_timbrado',
            field=models.DateField(default=datetime.datetime(2016, 8, 11, 12, 18, 28, 669000), help_text=b'Ingrese la Fecha de Autorizacion del Timbrado', verbose_name=b'Fecha de Autorizacion del Timbrado'),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 8, 11, 12, 18, 28, 669000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
    ]
