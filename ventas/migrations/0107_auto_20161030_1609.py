# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0106_auto_20161030_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='cierrecaja',
            name='total_efectivo',
            field=models.DecimalField(default=0, help_text=b'Corresponde a la suma del Monto de Apertura con el Monto Registrado en Efectivo.', verbose_name=b'Total Efectivo', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_fin_apertura_caja',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 31, 5, 9, 8, 781000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Apertura de Caja.', verbose_name=b'Fecha/hora Fin Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='fecha_hora_fin_jornada',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 31, 5, 9, 8, 783000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Jornada.', verbose_name=b'Fecha/hora Fin Jornada'),
        ),
    ]
