# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0215_auto_20161001_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 3, 17, 28, 56, 464000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='numero_orden_compra',
            field=models.AutoField(help_text=b'Este dato se genera automaticamente cada vez que se va crear una Orden de Compra.', serialize=False, verbose_name=b'Nro. Orden Compra', primary_key=True),
        ),
    ]
