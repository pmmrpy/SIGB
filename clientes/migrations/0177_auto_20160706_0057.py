# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0176_auto_20160706_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2016, 7, 6, 4, 57, 55, 849000, tzinfo=utc), help_text=b'Seleccione la fecha de nacimiento del Cliente.', verbose_name=b'Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 4, 57, 55, 852000, tzinfo=utc), help_text=b'Ingrese la fecha y hora de la Reserva.'),
        ),
    ]
