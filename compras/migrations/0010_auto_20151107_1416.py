# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0009_auto_20151107_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='telefonoproveedor',
            name='contacto',
            field=models.CharField(default=b'Nombre persona', help_text=b'Nombre de la persona a la cual contactar en este numero.', max_length=100),
        ),
        migrations.AddField(
            model_name='telefonoproveedor',
            name='interno',
            field=models.IntegerField(default=100, help_text=b'Ingrese el numero de interno.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 17, 16, 56, 909000, tzinfo=utc), help_text=b'Indique la fecha en la que el proveedor debe entregar el pedido.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 17, 16, 56, 909000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se realiza el pedido.'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='ruc',
            field=models.IntegerField(default=1, help_text=b'RUC del proveedor.', unique=True, max_length=8, verbose_name=b'RUC'),
        ),
    ]
