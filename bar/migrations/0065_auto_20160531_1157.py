# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0064_auto_20160531_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 31, 15, 57, 24, 682000, tzinfo=utc), help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual.'),
        ),
    ]
