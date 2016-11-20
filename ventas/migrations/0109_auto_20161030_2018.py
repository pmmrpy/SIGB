# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0275_horario_duracion_jornada'),
        ('ventas', '0108_auto_20161030_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='jornada',
            name='horario',
            field=models.ForeignKey(default=1, to='personal.Horario'),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='duracion_apertura',
            field=models.TimeField(default=datetime.time(10, 0), verbose_name=b'Duracion Apert. Caja'),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='estado_apertura_caja',
            field=models.CharField(max_length=3, verbose_name=b'Estado Apert. Caja', choices=[(b'VIG', b'Vigente'), (b'EXP', b'Expirada'), (b'CER', b'Cerrada')]),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_apertura_caja',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text=b'Fecha en la que se realiza la Apertura de Caja.', verbose_name=b'Fecha/hora Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_fin_apertura_caja',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 31, 9, 18, 10, 378000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Apertura de Caja.', verbose_name=b'Fecha/hora Fin Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_registro_apertura_caja',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha/hora registro Apert. Caja'),
        ),
        migrations.AlterField(
            model_name='cierrecaja',
            name='total_efectivo',
            field=models.DecimalField(default=0, verbose_name=b'Total Efectivo', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='fecha_hora_fin_jornada',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 31, 9, 18, 10, 382000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Jornada.', verbose_name=b'Fecha/hora Fin Jornada'),
        ),
    ]
