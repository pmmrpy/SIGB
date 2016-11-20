# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0081_auto_20161022_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='aperturacaja',
            name='duracion_apertura',
            field=models.TimeField(default=datetime.time(10, 0)),
        ),
        migrations.AddField(
            model_name='aperturacaja',
            name='fecha_hora_fin_apertura_caja',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 23, 3, 13, 56, 427000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Apertura de Caja.', verbose_name=b'Fecha/hora Fin Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='estado_apertura_caja',
            field=models.CharField(max_length=3, verbose_name=b'Estado', choices=[(b'VIG', b'Vigente'), (b'EXP', b'Expirada'), (b'CER', b'Cerrada')]),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='estado_jornada',
            field=models.CharField(max_length=3, verbose_name=b'Estado', choices=[(b'VIG', b'Vigente'), (b'EXP', b'Expirada'), (b'CER', b'Cerrada')]),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='fecha_hora_fin_jornada',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 23, 3, 13, 56, 430000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Jornada.', verbose_name=b'Fecha/hora Fin Jornada'),
        ),
    ]
