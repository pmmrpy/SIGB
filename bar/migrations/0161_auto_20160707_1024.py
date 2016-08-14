# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0160_auto_20160706_1317'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservaestado',
            options={'ordering': ('id',), 'verbose_name': 'Reserva - Estado', 'verbose_name_plural': 'Reservas - Estados'},
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 7, 14, 24, 1, 813000, tzinfo=utc), help_text=b'Registra la fecha y hora en la que se definio la Cotizacion. Corresponde a la fecha y hora actual.', verbose_name=b'Fecha de Cotizacion'),
        ),
    ]
