# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0066_auto_20151215_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 12, 15, 19, 41, 40, 959000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 15, 19, 41, 40, 962000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='pago',
            field=models.DecimalField(default=0, max_digits=18, decimal_places=0),
        ),
    ]
