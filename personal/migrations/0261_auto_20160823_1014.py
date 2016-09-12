# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0260_auto_20160817_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='sexo',
            field=models.CharField(help_text=b'Seleccione el sexo del Empleado.', max_length=1, verbose_name=b'Genero', choices=[(b'F', b'Femenino'), (b'M', b'Masculino'), (b'O', b'Otros')]),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2016, 8, 23, 14, 14, 10, 172000, tzinfo=utc), help_text=b'Ingrese la hora de finalizacion de la jornada de trabajo.', verbose_name=b'Hora de Finalizacion Jornada'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2016, 8, 23, 14, 14, 10, 172000, tzinfo=utc), help_text=b'Ingrese la hora de inicio de la jornada de trabajo.', verbose_name=b'Hora de Inicio Jornada'),
        ),
    ]
