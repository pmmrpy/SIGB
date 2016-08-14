# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0016_auto_20151108_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='compra_id',
        ),
        migrations.AddField(
            model_name='compra',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='numero_compra',
            field=models.IntegerField(default=1, help_text=b'Este dato se genera automaticamente cada vez que se va crearuna Orden de Compra.', verbose_name=b'Numero Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 8, 14, 56, 39, 465000, tzinfo=utc), help_text=b'Indique la fecha en la que el proveedor debe entregar el pedido.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 8, 14, 56, 39, 465000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se realiza el pedido.'),
        ),
    ]
