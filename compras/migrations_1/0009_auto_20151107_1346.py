# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0008_auto_20151107_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='ruc',
            field=models.IntegerField(default=1, help_text=b'RUC del proveedor.', unique=True, verbose_name=b'RUC'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 16, 46, 56, 773000, tzinfo=utc), help_text=b'Indique la fecha en la que el proveedor debe entregar el pedido.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 16, 46, 56, 773000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se realiza el pedido.'),
        ),
    ]
