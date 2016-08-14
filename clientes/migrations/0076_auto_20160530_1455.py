# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0075_auto_20160528_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2016, 5, 30, 18, 55, 19, 876000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='descripcion',
            field=models.CharField(default=b'Reserva de Mesa', help_text=b'Puede indicar alguna descripcion que identifique a la Reserva.', max_length=50),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 30, 18, 55, 19, 879000, tzinfo=utc), help_text=b'Ingrese la fech y hora de la Reserva.'),
        ),
    ]
