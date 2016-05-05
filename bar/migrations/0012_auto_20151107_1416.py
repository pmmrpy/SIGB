# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0011_auto_20151107_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codigociudadoperadoratelefono',
            name='ciudad_operadora',
            field=models.CharField(help_text=b'Descripcion de la ciudad o de la operadora de telefonia movil.', max_length=100, verbose_name=b'Descripcion Ciudad/Operadora'),
        ),
        migrations.AlterField(
            model_name='codigociudadoperadoratelefono',
            name='codigo_ciudad_operadora_telefono',
            field=models.IntegerField(default=21, help_text=b'Codigo de ciudad o de la operadora de telefonia movil.', verbose_name=b'Codigo Ciudad/Operadora'),
        ),
        migrations.AlterField(
            model_name='codigopaistelefono',
            name='codigo_pais_telefono',
            field=models.IntegerField(default=595, help_text=b'Codigo internacional del pais al cual corresponde el telefono.', verbose_name=b'Codigo Pais'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 17, 16, 56, 850000, tzinfo=utc), help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual'),
        ),
    ]
