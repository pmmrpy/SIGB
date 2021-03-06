# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0046_auto_20160524_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 24, 17, 38, 53, 417000, tzinfo=utc), help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual.'),
        ),
    ]
