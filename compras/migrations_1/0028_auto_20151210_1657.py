# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0027_auto_20151112_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 10, 19, 56, 49, 699000, tzinfo=utc), help_text=b'Indique la fecha en la que el proveedor debe entregar el pedido.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 10, 19, 56, 49, 699000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se realiza el pedido.'),
        ),
        migrations.AlterField(
            model_name='telefonoproveedor',
            name='telefono',
            field=models.IntegerField(help_text=b'Ingrese el telefono fijo o movil del proveedor. El dato debe contener solo numeros.'),
        ),
    ]
