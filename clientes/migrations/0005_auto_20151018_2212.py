# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20151018_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='usuario_registro',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 10, 19, 1, 12, 57, 712000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 19, 1, 12, 57, 714000, tzinfo=utc)),
        ),
    ]
