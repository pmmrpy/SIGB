# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0234_auto_20160813_1644'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reserva',
            options={'verbose_name': 'Reserva de Mesa', 'verbose_name_plural': 'Reservas de Mesas'},
        ),
        migrations.AlterField(
            model_name='reserva',
            name='cantidad_personas',
            field=models.PositiveIntegerField(help_text=b'Ingrese la cantidad de personas que utilizaran la Reserva.', verbose_name=b'Cantidad de Personas'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora_reserva',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 13, 21, 58, 45, 360000, tzinfo=utc), help_text=b'Ingrese la fecha y hora de la Reserva.', verbose_name=b'Fecha y hora para la Reserva.'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='usuario_registro',
            field=models.ForeignKey(verbose_name=b'Usuario que registra Reserva', to=settings.AUTH_USER_MODEL, help_text=b'Este dato se completara automaticamente cuando la Reserva sea guardada.'),
        ),
    ]
