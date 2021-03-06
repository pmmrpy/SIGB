# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0112_auto_20160622_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 23, 3, 56, 39, 562000, tzinfo=utc), help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual.'),
        ),
    ]
