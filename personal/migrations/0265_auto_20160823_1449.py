# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0264_auto_20160823_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='salario',
            field=models.DecimalField(default=1824055, help_text=b'Ingrese el salario del Empleado.', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2016, 8, 23, 18, 49, 34, 274000, tzinfo=utc), help_text=b'Ingrese la hora de finalizacion de la jornada de trabajo.', verbose_name=b'Hora de Finalizacion Jornada'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2016, 8, 23, 18, 49, 34, 274000, tzinfo=utc), help_text=b'Ingrese la hora de inicio de la jornada de trabajo.', verbose_name=b'Hora de Inicio Jornada'),
        ),
    ]
