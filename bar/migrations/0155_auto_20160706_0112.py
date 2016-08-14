# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0154_auto_20160706_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 5, 12, 35, 814000, tzinfo=utc), help_text=b'Registra la fecha y hora en la que se definio la Cotizacion. Corresponde a la fecha y hora actual.', verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='reservaestado',
            name='reserva_estado',
            field=models.CharField(help_text=b'Ingrese el identificador del Estado de la Reserva. (Hasta 2 caracteres)', max_length=2, verbose_name=b'Estado de la Reserva', choices=[(b'VI', b'Vigente'), (b'CA', b'Caducada'), (b'UT', b'Utilizada')]),
        ),
    ]
