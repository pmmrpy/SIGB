# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0016_auto_20151024_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 10, 25, 14, 38, 20, 821000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 14, 38, 20, 825000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='mesas',
            field=models.ManyToManyField(to='bar.Mesa'),
        ),
    ]
