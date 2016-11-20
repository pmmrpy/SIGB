# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0109_auto_20161030_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_fin_apertura_caja',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 31, 11, 41, 58, 849000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Apertura de Caja.', verbose_name=b'Fecha/hora Fin Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='estado_jornada',
            field=models.CharField(blank=True, max_length=3, verbose_name=b'Estado', choices=[(b'VIG', b'Vigente'), (b'EXP', b'Expirada'), (b'CER', b'Cerrada')]),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='fecha_hora_fin_jornada',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 31, 11, 41, 58, 854000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Jornada.', verbose_name=b'Fecha/hora Fin Jornada'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='horario',
            field=models.ForeignKey(to='personal.Horario'),
        ),
    ]
