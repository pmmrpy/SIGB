# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_auto_20151025_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='fecha',
        ),
        migrations.AddField(
            model_name='compra',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 1, 28, 57, 262000, tzinfo=utc), help_text=b'Indique la fecha en la que el proveedor debe entregar el pedido.'),
        ),
        migrations.AddField(
            model_name='compra',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 1, 28, 57, 262000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se realiza el pedido.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(help_text=b'Seleccione el proveedor al cual se le realizara la compra.', to='compras.Proveedor'),
        ),
    ]
