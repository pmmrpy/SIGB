# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0185_auto_20160910_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='disponible_linea_credito_proveedor',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente como la diferencia entre el Monto de la Linea de Credito y el Monto Utilizado de la Linea de Credito.', verbose_name=b'Disponible Linea de Credito', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(to='compras.Proveedor'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 11, 21, 59, 18, 853000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
    ]
