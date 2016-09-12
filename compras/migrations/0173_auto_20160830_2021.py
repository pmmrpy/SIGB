# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0172_auto_20160830_1917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proveedor',
            old_name='ciudad_proveedor',
            new_name='ciudad',
        ),
        migrations.RenameField(
            model_name='proveedor',
            old_name='pais_proveedor',
            new_name='pais',
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 1, 0, 21, 33, 364000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
    ]
