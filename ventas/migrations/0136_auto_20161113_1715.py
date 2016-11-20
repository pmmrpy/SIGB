# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0135_auto_20161113_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_fin_apertura_caja',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 14, 6, 15, 32, 168000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Apertura de Caja.', verbose_name=b'Fecha/hora Fin Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='fecha_hora_fin_jornada',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 14, 6, 15, 32, 171000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Jornada.', verbose_name=b'Fecha/hora Fin Jornada'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='cliente_documento_factura',
            field=models.CharField(help_text=b'Seleccione el Documento del Cliente el cual se registrara en la factura.', max_length=50, null=True, verbose_name=b'Documento Factura', blank=True),
        ),
    ]
