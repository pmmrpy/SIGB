# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0281_auto_20161106_1501'),
        ('ventas', '0124_auto_20161105_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='fecha_hora_cancelacion',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='motivo_cancelacion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='observaciones_cancelacion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='usuario_cancelacion',
            field=models.ForeignKey(related_name='usuario_cancelacion_venta', blank=True, to='personal.Empleado', help_text=b'Usuario que cancelo la Venta.', null=True, verbose_name=b'Cancelado por?'),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_fin_apertura_caja',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 7, 4, 0, 59, 411000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Apertura de Caja.', verbose_name=b'Fecha/hora Fin Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='fecha_hora_fin_jornada',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 7, 4, 0, 59, 413000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Jornada.', verbose_name=b'Fecha/hora Fin Jornada'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha_hora_venta',
            field=models.DateTimeField(help_text=b'Registra la fecha y hora en la que se confirmo la Venta.', verbose_name=b'Fecha/hora de la Venta', auto_now=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='numero_pedido',
            field=models.OneToOneField(blank=True, to='ventas.Pedido', help_text=b'Seleccione el Numero de Pedido para el cual se registrara la Venta.', verbose_name=b'Numero de Pedido'),
        ),
    ]
