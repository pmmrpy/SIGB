# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0006_auto_20151106_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 2, 0, 44, 493000, tzinfo=utc), help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual'),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='abreviacion_moneda',
            field=models.CharField(default=b'US$', help_text=b'Abreviacion o simbolode la moneda. EJ: Guaranies - Gs.', max_length=5),
        ),
    ]
