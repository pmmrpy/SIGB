# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0274_auto_20161010_1636'),
        ('ventas', '0080_auto_20161018_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_hora_inicio_jornada', models.DateTimeField(help_text=b'Fecha/hora de Inicio de la Jornada.', verbose_name=b'Fecha/hora Inicio Jornada', auto_now_add=True)),
                ('duracion_jornada', models.TimeField(default=datetime.time(10, 0))),
                ('fecha_hora_fin_jornada', models.DateTimeField(default=datetime.datetime(2016, 10, 23, 1, 31, 54, 39000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Jornada.', verbose_name=b'Fecha/hora Fin Jornada')),
                ('estado_jornada', models.CharField(max_length=3, verbose_name=b'Estado', choices=[(b'VIG', b'Vigente'), (b'CER', b'Cerrada')])),
                ('cantidad_pedidos_procesados', models.PositiveIntegerField(null=True, blank=True)),
                ('cantidad_pedidos_pendientes', models.PositiveIntegerField(null=True, blank=True)),
                ('fecha_hora_cierre_jornada', models.DateTimeField(help_text=b'Fecha/hora de Cierre de la Jornada.', null=True, verbose_name=b'Fecha/hora Cierre Jornada', blank=True)),
                ('mozo', models.ForeignKey(verbose_name=b'Mozo', to='personal.Empleado', help_text=b'Se define de acuerdo al usuario logueado al Sistema.')),
            ],
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado_pedido',
            field=models.ForeignKey(verbose_name=b'Estado del Pedido', to='bar.PedidoEstado', help_text=b'El estado del Pedido se establece automaticamente.'),
        ),
        migrations.CreateModel(
            name='FinJornada',
            fields=[
            ],
            options={
                'verbose_name': 'Mozos - Cierre de Jornada',
                'proxy': True,
                'verbose_name_plural': 'Mozos - Cierres de Jornadas',
            },
            bases=('ventas.jornada',),
        ),
        migrations.CreateModel(
            name='InicioJornada',
            fields=[
            ],
            options={
                'verbose_name': 'Mozos - Inicio de Jornada',
                'proxy': True,
                'verbose_name_plural': 'Mozos - Inicios de Jornadas',
            },
            bases=('ventas.jornada',),
        ),
    ]
