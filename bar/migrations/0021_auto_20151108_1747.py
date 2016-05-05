# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0020_auto_20151108_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 8, 20, 47, 36, 947000, tzinfo=utc), help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual'),
        ),
        migrations.AlterField(
            model_name='formapagocompra',
            name='plazo_compra',
            field=models.IntegerField(help_text=b'En caso de Credito establecer el plazo de tiempo en d\xc3\xadas para el pago.'),
        ),
    ]
