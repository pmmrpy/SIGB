# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0196_auto_20160722_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2016, 7, 27, 0, 39, 58, 143000, tzinfo=utc), help_text=b'Seleccione la fecha de nacimiento del Cliente.', verbose_name=b'Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 27, 0, 39, 58, 145000, tzinfo=utc), help_text=b'Ingrese la fecha y hora de la Reserva.'),
        ),
    ]
