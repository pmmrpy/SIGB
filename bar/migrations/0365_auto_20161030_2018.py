# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0364_auto_20161030_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja',
            name='estado_caja',
            field=models.CharField(default=b'CER', help_text=b'Seleccione el identificador del Estado de la Caja.', max_length=3, verbose_name=b'Estado Caja', choices=[(b'ABI', b'Abierta'), (b'CER', b'Cerrada'), (b'CLA', b'Clausurada')]),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 10, 30, 20, 18, 10, 57000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
    ]
