# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0308_auto_20161119_0900'),
        ('stock', '0215_auto_20161118_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='transferenciastock',
            name='fecha_hora_cancelacion',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='transferenciastock',
            name='motivo_cancelacion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='transferenciastock',
            name='observaciones_cancelacion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='transferenciastock',
            name='usuario_cancelacion',
            field=models.ForeignKey(related_name='usuario_cancelacion_transferencia', blank=True, to='personal.Empleado', help_text=b'Usuario que cancelo la Transferencia.', null=True, verbose_name=b'Cancelado por?'),
        ),
        migrations.AlterField(
            model_name='transferenciastock',
            name='estado_transferencia',
            field=models.ForeignKey(default=2, verbose_name=b'Estado Transferencia', to='bar.TransferenciaStockEstado', help_text=b'El estado de la Transferencia se asigna de forma automatica.'),
        ),
    ]
