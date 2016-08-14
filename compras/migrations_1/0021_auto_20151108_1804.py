# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0020_auto_20151108_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 8, 21, 4, 8, 412000, tzinfo=utc), help_text=b'Indique la fecha en la que el proveedor debe entregar el pedido.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 8, 21, 4, 8, 412000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se realiza el pedido.'),
        ),
        migrations.AlterField(
            model_name='telefonoproveedor',
            name='contacto',
            field=models.CharField(help_text=b'Nombre de la persona a la cual contactar en este numero.', max_length=100),
        ),
        migrations.AlterField(
            model_name='telefonoproveedor',
            name='interno',
            field=models.IntegerField(help_text=b'Ingrese el numero de interno.', null=True, blank=True),
        ),
    ]
