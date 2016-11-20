# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0111_auto_20161031_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aperturacaja',
            name='duracion_apertura',
            field=models.TimeField(verbose_name=b'Duracion Apert. Caja'),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_fin_apertura_caja',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 1, 6, 22, 3, 717000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Apertura de Caja.', verbose_name=b'Fecha/hora Fin Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='sector',
            field=models.ForeignKey(help_text=b'Seleccione el Sector en donde desempenara sus funciones el Empleado.', to='bar.Sector'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='fecha_hora_fin_jornada',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 1, 6, 22, 3, 722000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Jornada.', verbose_name=b'Fecha/hora Fin Jornada'),
        ),
    ]
