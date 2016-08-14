# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0180_auto_20160731_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 31, 23, 50, 44, 460000, tzinfo=utc), help_text=b'Registra la fecha y hora en la que se definio la Cotizacion. Corresponde a la fecha y hora actual.', verbose_name=b'Fecha de Cotizacion'),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='timbrado',
            field=models.DecimalField(default=1, help_text=b'Ingrese el numero de Timbrado.', verbose_name=b'Numero de Timbrado', max_digits=8, decimal_places=0),
        ),
    ]
