# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0126_auto_20161109_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cierrecaja',
            name='cantidad_operaciones_otros_medios',
        ),
        migrations.RemoveField(
            model_name='cierrecaja',
            name='cantidad_operaciones_tcs',
        ),
        migrations.RemoveField(
            model_name='cierrecaja',
            name='cantidad_operaciones_tds',
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='cantidad_operaciones_otros_medios_canceladas',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Cant. Oper. Otros Medios Canceladas'),
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='cantidad_operaciones_otros_medios_pendientes',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Cant. Oper. Otros Medios Pendientes'),
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='cantidad_operaciones_otros_medios_procesadas',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Cant. Oper. Otros Medios Procesadas'),
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='cantidad_operaciones_tcs_canceladas',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Cant. Oper. TCs Canceladas'),
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='cantidad_operaciones_tcs_pendientes',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Cant. Oper. TCs Pendientes'),
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='cantidad_operaciones_tcs_procesadas',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Cant. Oper. TCs Procesadas'),
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='cantidad_operaciones_tds_canceladas',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Cant. Oper. TDs Canceladas'),
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='cantidad_operaciones_tds_pendientes',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Cant. Oper. TDs Pendientes'),
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='cantidad_operaciones_tds_procesadas',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Cant. Oper. TDs Procesadas'),
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='cantidad_total_operaciones_canceladas',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Cant. Total Oper. Canceladas'),
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='cantidad_total_operaciones_pendientes',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Cant. Total Oper. Pendientes'),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_fin_apertura_caja',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 11, 2, 20, 55, 97000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Apertura de Caja.', verbose_name=b'Fecha/hora Fin Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='fecha_hora_fin_jornada',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 11, 2, 20, 55, 100000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Jornada.', verbose_name=b'Fecha/hora Fin Jornada'),
        ),
    ]
