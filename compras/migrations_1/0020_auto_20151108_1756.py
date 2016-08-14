# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0019_auto_20151108_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 8, 20, 56, 47, 771000, tzinfo=utc), help_text=b'Indique la fecha en la que el proveedor debe entregar el pedido.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 8, 20, 56, 47, 771000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se realiza el pedido.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='numero_compra',
            field=models.IntegerField(default=1, help_text=b'Este dato se genera automaticamente cada vez que se va crear una Orden de Compra.', unique=True, verbose_name=b'Numero Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='digito_verificador',
            field=models.IntegerField(default=1, help_text=b'Ingrese el digito verificador del RUC del proveedor.'),
        ),
        migrations.AlterField(
            model_name='telefonoproveedor',
            name='contacto',
            field=models.CharField(help_text=b'Nombre de la persona a la cual contactar en este numero.', max_length=100, blank=True),
        ),
    ]
