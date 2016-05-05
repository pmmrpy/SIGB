# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0018_auto_20151108_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 8, 20, 47, 36, 986000, tzinfo=utc), help_text=b'Indique la fecha en la que el proveedor debe entregar el pedido.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 8, 20, 47, 36, 985000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se realiza el pedido.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='numero_compra',
            field=models.IntegerField(default=1, help_text=b'Este dato se genera automaticamente cada vez que se va crear una Orden de Compra.', verbose_name=b'Numero Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='ruc',
            field=models.CharField(help_text=b'RUC del proveedor.', unique=True, max_length=15, verbose_name=b'RUC'),
        ),
        migrations.AlterField(
            model_name='telefonoproveedor',
            name='codigo_ciudad_operadora_telefono',
            field=models.ForeignKey(default=21, to='bar.CodigoCiudadOperadoraTelefono', help_text=b'Seleccione o ingrese el codigo de ciudad u operadora de telefonia movil.'),
        ),
        migrations.AlterField(
            model_name='telefonoproveedor',
            name='contacto',
            field=models.CharField(default=b'Nombre persona', help_text=b'Nombre de la persona a la cual contactar en este numero.', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='telefonoproveedor',
            name='interno',
            field=models.IntegerField(help_text=b'Ingrese el numero de interno.', blank=True),
        ),
    ]
