# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0176_auto_20160905_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='estado_linea_credito_proveedor',
            field=models.CharField(blank=True, help_text=b'Se asigna automaticamente de acuerdo a la utilizacion de la Linea de Credito.', max_length=3, verbose_name=b'Estado Linea de Credito', choices=[(b'DEL', b'Dentro de la Linea de Credito'), (b'LIM', b'En el Limite'), (b'SOB', b'Sobregirada')]),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 6, 20, 36, 28, 428000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
    ]
