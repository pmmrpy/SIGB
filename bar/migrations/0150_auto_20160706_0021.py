# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0149_auto_20160706_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja',
            name='numero_caja',
            field=models.PositiveIntegerField(help_text=b'Ingrese el Numero de Caja.', unique=True, verbose_name=b'Numero de Caja'),
        ),
        migrations.AlterField(
            model_name='caja',
            name='ubicacion',
            field=models.OneToOneField(to='bar.CajaUbicacion'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 4, 21, 15, 298000, tzinfo=utc), help_text=b'Registra la fecha y hora en la que se definio la Cotizacion. Corresponde a la fecha y hora actual.', verbose_name=b''),
        ),
    ]
