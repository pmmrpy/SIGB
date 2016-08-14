# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0228_auto_20160813_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2016, 8, 13, 14, 20, 23, 639000, tzinfo=utc), help_text=b'Seleccione la fecha de nacimiento del Cliente.', verbose_name=b'Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora_reserva',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 13, 14, 20, 23, 641000, tzinfo=utc), help_text=b'Ingrese la fecha y hora de la Reserva.', verbose_name=b'Fecha y hora para la Reserva.'),
        ),
    ]
