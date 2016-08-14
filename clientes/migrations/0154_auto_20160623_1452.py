# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0153_auto_20160623_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2016, 6, 23, 18, 52, 23, 757000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 23, 18, 52, 23, 760000, tzinfo=utc), help_text=b'Ingrese la fech y hora de la Reserva.'),
        ),
    ]
