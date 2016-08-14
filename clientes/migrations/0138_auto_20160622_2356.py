# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0137_auto_20160622_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2016, 6, 23, 3, 56, 39, 569000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 23, 3, 56, 39, 572000, tzinfo=utc), help_text=b'Ingrese la fech y hora de la Reserva.'),
        ),
    ]
