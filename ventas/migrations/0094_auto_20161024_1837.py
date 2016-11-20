# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0093_auto_20161024_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_apertura_caja',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text=b'Fecha en la que se realiza la Apertura de Caja.', verbose_name=b'Fecha Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_fin_apertura_caja',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 25, 7, 37, 8, 836000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Apertura de Caja.', verbose_name=b'Fecha/hora Fin Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='fecha_hora_fin_jornada',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 25, 7, 37, 8, 838000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Jornada.', verbose_name=b'Fecha/hora Fin Jornada'),
        ),
    ]
