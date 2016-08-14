# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0235_auto_20160813_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='cantidad_personas',
            field=models.PositiveIntegerField(default=0, help_text=b'Ingrese la cantidad de personas que utilizaran la Reserva.', verbose_name=b'Cantidad de Personas'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora_reserva',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 14, 15, 20, 12, 910000, tzinfo=utc), help_text=b'Ingrese la fecha y hora de la Reserva.', verbose_name=b'Fecha y hora para la Reserva.'),
        ),
    ]
