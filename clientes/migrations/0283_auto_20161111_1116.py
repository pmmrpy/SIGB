# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0282_reserva_cliente_documento_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='cliente_documento_reserva',
            field=models.CharField(default=b'1234569', help_text=b'Seleccione el Documento del Cliente el cual se registrara en la Reserva.', max_length=50, verbose_name=b'Documento'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora_reserva',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text=b'Ingrese la fecha y hora de la Reserva. Se pueden realizar Reservas de Mesas desde las 18:00 hs hasta las 21:00 hs.', verbose_name=b'Fecha y hora para la Reserva.'),
        ),
    ]
