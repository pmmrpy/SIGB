# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0128_auto_20161110_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_fin_apertura_caja',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 12, 0, 16, 6, 436000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Apertura de Caja.', verbose_name=b'Fecha/hora Fin Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='cierrecaja',
            name='rendicion_efectivo',
            field=models.DecimalField(default=0, help_text=b'', verbose_name=b'Monto Rendicion Efectivo', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='fecha_hora_fin_jornada',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 12, 0, 16, 6, 439000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Jornada.', verbose_name=b'Fecha/hora Fin Jornada'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='apertura_caja',
            field=models.ForeignKey(verbose_name=b'Apertura de Caja', to='ventas.AperturaCaja', help_text=b'Este valor se asigna dependiendo del usuario logueado y de si posee una Apertura de Caja vigente.'),
        ),
    ]
