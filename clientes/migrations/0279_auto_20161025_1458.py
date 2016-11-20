# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0278_auto_20161025_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='hora_fin_reservas',
            field=models.TimeField(default=datetime.time(21, 0)),
        ),
        migrations.AddField(
            model_name='reserva',
            name='hora_inicio_reservas',
            field=models.TimeField(default=datetime.time(18, 0)),
        ),
    ]
