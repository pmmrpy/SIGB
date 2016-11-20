# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0348_auto_20161024_1748'),
        ('ventas', '0091_auto_20161024_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='jornada',
            name='sector',
            field=models.ForeignKey(default=2, to='bar.Sector', help_text=b'Seleccione el Sector en donde desempenara sus funciones el Empleado.'),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_fin_apertura_caja',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 25, 6, 48, 32, 639000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Apertura de Caja.', verbose_name=b'Fecha/hora Fin Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='fecha_hora_fin_jornada',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 25, 6, 48, 32, 641000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Jornada.', verbose_name=b'Fecha/hora Fin Jornada'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='fecha_hora_inicio_jornada',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text=b'Fecha/hora de Inicio de la Jornada.', verbose_name=b'Fecha/hora Inicio Jornada'),
        ),
    ]
