# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0274_auto_20161010_1636'),
        ('ventas', '0104_auto_20161029_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='cierrecaja',
            name='usuario_cierre_caja',
            field=models.ForeignKey(related_name='usuario_cierre_caja', blank=True, to='personal.Empleado', help_text=b'Usuario que realizo el Cierre de Caja.', null=True, verbose_name=b'Cierre de Caja realizado por?'),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_fin_apertura_caja',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 31, 0, 56, 29, 890000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Apertura de Caja.', verbose_name=b'Fecha/hora Fin Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='cierrecaja',
            name='cantidad_operaciones_efectivo',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Cant. Oper. Efectivo'),
        ),
        migrations.AlterField(
            model_name='cierrecaja',
            name='cantidad_operaciones_otros_medios',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Cant. Oper. Otros Medios'),
        ),
        migrations.AlterField(
            model_name='cierrecaja',
            name='cantidad_operaciones_tcs',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Cant. Oper. TCs'),
        ),
        migrations.AlterField(
            model_name='cierrecaja',
            name='cantidad_operaciones_tds',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Cant. Oper. TDs'),
        ),
        migrations.AlterField(
            model_name='cierrecaja',
            name='fecha_hora_registro_cierre_caja',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Fecha/hora registro Cierre de Caja'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='fecha_hora_fin_jornada',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 31, 0, 56, 29, 893000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Jornada.', verbose_name=b'Fecha/hora Fin Jornada'),
        ),
    ]
