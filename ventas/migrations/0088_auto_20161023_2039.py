# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0087_auto_20161023_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='jornada',
            field=models.ForeignKey(default=1, verbose_name=b'Jornada', to='ventas.InicioJornada', help_text=b'Se asigna dependiendo del usuario logueado y de si posee una Jornada vigente.'),
        ),
        migrations.AddField(
            model_name='venta',
            name='efectivo_recibido',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=18, blank=True, null=True, verbose_name=b'Efectivo Recibido'),
        ),
        migrations.AddField(
            model_name='venta',
            name='vuelto',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=18, blank=True, null=True, verbose_name=b'Vuelto'),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_fin_apertura_caja',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 24, 9, 39, 32, 123000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Apertura de Caja.', verbose_name=b'Fecha/hora Fin Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='cantidad_pedidos_cancelados',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Cant. Pedidos Cancelados', blank=True),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='cantidad_pedidos_pendientes',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Cant. Pedidos Pendientes', blank=True),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='cantidad_pedidos_procesados',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Cant. Pedidos Procesados', blank=True),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='duracion_jornada',
            field=models.TimeField(default=datetime.time(10, 0), verbose_name=b'Duracion Jornada'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='fecha_hora_fin_jornada',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 24, 9, 39, 32, 127000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Jornada.', verbose_name=b'Fecha/hora Fin Jornada'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='apertura_caja',
            field=models.ForeignKey(verbose_name=b'Apertura de Caja', to='ventas.AperturaCaja', help_text=b'Se asigna dependiendo del usuario logueado y de si posee una Apertura de Caja vigente.'),
        ),
    ]
