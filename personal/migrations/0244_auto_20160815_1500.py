# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0243_auto_20160815_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='cargo',
            field=models.CharField(help_text=b'Ingrese el identificador del Cargo. (Hasta 2 caracteres)', max_length=2, verbose_name=b'Cargo', choices=[(b'MO', b'Moz@'), (b'BM', b'Barman/Barwoman'), (b'CA', b'Cajer@'), (b'CO', b'Cociner@'), (b'DE', b'Depositer@'), (b'EI', b'Encargado Informatica'), (b'RP', b'Relaciones Publicas')]),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2016, 8, 15, 19, 0, 5, 419000, tzinfo=utc), help_text=b'Ingrese la hora de finalizacion de la jornada de trabajo.', verbose_name=b'Hora de Finalizacion Jornada'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2016, 8, 15, 19, 0, 5, 419000, tzinfo=utc), help_text=b'Ingrese la hora de inicio de la jornada de trabajo.', verbose_name=b'Hora de Inicio Jornada'),
        ),
    ]
