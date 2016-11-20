# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0082_auto_20161022_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aperturacaja',
            name='duracion_apertura',
            field=models.TimeField(default=datetime.time(10, 0), verbose_name=b'Duracion Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_apertura_caja',
            field=models.DateTimeField(help_text=b'Fecha en la que se realiza la Apertura de Caja.', verbose_name=b'Fecha Apertura Caja', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_fin_apertura_caja',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 23, 6, 2, 48, 796000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Apertura de Caja.', verbose_name=b'Fecha/hora Fin Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='fecha_hora_fin_jornada',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 23, 6, 2, 48, 799000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Jornada.', verbose_name=b'Fecha/hora Fin Jornada'),
        ),
    ]
