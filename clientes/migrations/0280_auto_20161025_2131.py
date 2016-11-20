# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0274_auto_20161010_1636'),
        ('clientes', '0279_auto_20161025_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='fecha_hora_cancelacion',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='motivo_cancelacion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='observaciones_cancelacion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='usuario_cancelacion',
            field=models.ForeignKey(related_name='usuario_cancelacion_reserva', blank=True, to='personal.Empleado', help_text=b'Usuario que cancelo la Reserva.', null=True, verbose_name=b'Cancelado por?'),
        ),
    ]
