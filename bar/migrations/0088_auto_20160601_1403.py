# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0087_auto_20160601_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 1, 18, 3, 26, 199000, tzinfo=utc), help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual.'),
        ),
    ]