# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0134_auto_20161112_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_fin_apertura_caja',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 14, 3, 18, 58, 436000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Apertura de Caja.', verbose_name=b'Fecha/hora Fin Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='cierrecaja',
            name='cantidad_total_operaciones_canceladas',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Ventas Canceladas'),
        ),
        migrations.AlterField(
            model_name='cierrecaja',
            name='cantidad_total_operaciones_pendientes',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Ventas Pendientes'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='fecha_hora_fin_jornada',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 14, 3, 18, 58, 441000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Jornada.', verbose_name=b'Fecha/hora Fin Jornada'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='forma_pago',
            field=models.CharField(choices=[(b'EF', b'Efectivo'), (b'TC', b'Tarjeta de Credito'), (b'TD', b'Tarjeta de Debito'), (b'OM', b'Otros medios')], max_length=2, blank=True, help_text=b'Seleccione la Forma de Pago.', null=True, verbose_name=b'Forma de Pago'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='numero_pedido',
            field=models.ForeignKey(verbose_name=b'Numero de Pedido', to='ventas.Pedido', help_text=b'Seleccione el Numero de Pedido para el cual se registrara la Venta.'),
        ),
    ]
