# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0037_auto_20151107_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 11, 7, 17, 36, 17, 45000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='clientedocumento',
            name='numero_documento',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 17, 36, 17, 50000, tzinfo=utc)),
        ),
    ]
