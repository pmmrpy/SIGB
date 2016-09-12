# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0248_auto_20160815_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora_reserva',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 15, 19, 9, 24, 885000, tzinfo=utc), help_text=b'Ingrese la fecha y hora de la Reserva.', verbose_name=b'Fecha y hora para la Reserva.'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='usuario_registro',
            field=models.ForeignKey(verbose_name=b'Usuario que registra Reserva', to='personal.Empleado', help_text=b'Este dato se completara automaticamente cuando la Reserva sea guardada.'),
        ),
    ]
