# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0103_auto_20161025_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='cierrecaja',
            name='cantidad_operaciones_efectivo',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='cantidad_operaciones_otros_medios',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='cantidad_operaciones_tcs',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='cantidad_operaciones_tds',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_fin_apertura_caja',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 30, 9, 34, 8, 984000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Apertura de Caja.', verbose_name=b'Fecha/hora Fin Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='cierrecaja',
            name='apertura_caja',
            field=models.ForeignKey(verbose_name=b'Apertura de Caja', to='ventas.AperturaCaja', help_text=b'Seleccione la Apertura de Caja para la cual se realizara el cierre.'),
        ),
        migrations.AlterField(
            model_name='cierrecaja',
            name='fecha_hora_registro_cierre_caja',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha/hora registro Cierre de Caja'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='fecha_hora_fin_jornada',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 30, 9, 34, 8, 987000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Jornada.', verbose_name=b'Fecha/hora Fin Jornada'),
        ),
    ]
