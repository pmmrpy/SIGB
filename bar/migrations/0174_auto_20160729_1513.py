# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0173_auto_20160726_2040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timbrado',
            old_name='fecha_fin_timbrado',
            new_name='fecha_autorizacion_timbrado',
        ),
        migrations.RenameField(
            model_name='timbrado',
            old_name='fecha_inicio_timbrado',
            new_name='fecha_limite_vigencia_timbrado',
        ),
        migrations.AddField(
            model_name='timbrado',
            name='timbrado',
            field=models.PositiveIntegerField(default=1, help_text=b'Ingrese el numero de Timbrado.', max_length=8, verbose_name=b'Numero de Timbrado'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 29, 19, 13, 50, 342000, tzinfo=utc), help_text=b'Registra la fecha y hora en la que se definio la Cotizacion. Corresponde a la fecha y hora actual.', verbose_name=b'Fecha de Cotizacion'),
        ),
    ]
