# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0086_auto_20161023_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='jornada',
            name='cantidad_pedidos_cancelados',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Cantidad Pedidos Cancelados', blank=True),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_fin_apertura_caja',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 24, 8, 20, 1, 791000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Apertura de Caja.', verbose_name=b'Fecha/hora Fin Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='fecha_hora_fin_jornada',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 24, 8, 20, 1, 793000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Jornada.', verbose_name=b'Fecha/hora Fin Jornada'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='usuario_cierre_jornada',
            field=models.ForeignKey(related_name='usuario_cierre_jornada', blank=True, to='personal.Empleado', help_text=b'Usuario que realizo el Cierre de la Jornada.', null=True, verbose_name=b'Cerrado por?'),
        ),
    ]
