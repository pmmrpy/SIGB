# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0079_auto_20160530_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2016, 5, 31, 4, 22, 35, 29000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 31, 4, 22, 35, 31000, tzinfo=utc), help_text=b'Ingrese la fech y hora de la Reserva.'),
        ),
    ]
