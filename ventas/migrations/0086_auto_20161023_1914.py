# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0274_auto_20161010_1636'),
        ('ventas', '0085_auto_20161022_1709'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='finjornada',
            options={'verbose_name': 'Mozos/Barmans - Cierre de Jornada', 'verbose_name_plural': 'Mozos/Barmans - Cierres de Jornadas'},
        ),
        migrations.AlterModelOptions(
            name='iniciojornada',
            options={'verbose_name': 'Mozos/Barmans - Inicio de Jornada', 'verbose_name_plural': 'Mozos/Barmans - Inicios de Jornadas'},
        ),
        migrations.AddField(
            model_name='jornada',
            name='usuario_cierre_jornada',
            field=models.ForeignKey(related_name='usuario_cierre_jornada', default=17, to='personal.Empleado', blank=True, help_text=b'Usuario que realizo el Cierre de la Jornada.', null=True, verbose_name=b'Cerrado por?'),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_fin_apertura_caja',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 24, 8, 14, 46, 871000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Apertura de Caja.', verbose_name=b'Fecha/hora Fin Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='cantidad_pedidos_pendientes',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Cantidad Pedidos Pendientes', blank=True),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='cantidad_pedidos_procesados',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Cantidad Pedidos Procesados', blank=True),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='fecha_hora_fin_jornada',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 24, 8, 14, 46, 873000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Jornada.', verbose_name=b'Fecha/hora Fin Jornada'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='mozo',
            field=models.ForeignKey(related_name='mozo', verbose_name=b'Mozo/Barman', to='personal.Empleado', help_text=b'Se define de acuerdo al usuario logueado al Sistema.'),
        ),
    ]
