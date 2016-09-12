# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0264_auto_20160817_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(help_text=b'Seleccione el genero del Cliente.', max_length=1, verbose_name=b'Genero', choices=[(b'F', b'Femenino'), (b'M', b'Masculino'), (b'O', b'Otros')]),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora_reserva',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 23, 14, 14, 10, 176000, tzinfo=utc), help_text=b'Ingrese la fecha y hora de la Reserva.', verbose_name=b'Fecha y hora para la Reserva.'),
        ),
    ]
