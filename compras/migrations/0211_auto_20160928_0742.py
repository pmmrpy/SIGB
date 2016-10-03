# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0294_auto_20160928_0742'),
        ('compras', '0210_auto_20160927_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='timbrado',
            field=models.ForeignKey(default=1, to='bar.Timbrado'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 29, 11, 42, 26, 656000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
    ]
