# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20150928_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 9, 28, 5, 42, 4, 257000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='estado',
            field=models.ForeignKey(to='clientes.ReservaEstado'),
        ),
    ]
