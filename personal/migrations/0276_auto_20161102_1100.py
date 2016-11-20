# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0275_horario_duracion_jornada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='duracion_jornada',
            field=models.TimeField(default=datetime.time(8, 0), verbose_name=b'Duracion Jornada'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2016, 11, 2, 22, 0, 40, 615000, tzinfo=utc), help_text=b'Ingrese la hora de finalizacion de la jornada de trabajo.', verbose_name=b'Hora de Finalizacion Jornada'),
        ),
    ]
