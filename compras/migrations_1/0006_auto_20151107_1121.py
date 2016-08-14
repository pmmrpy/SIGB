# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0008_auto_20151107_1121'),
        ('compras', '0005_auto_20151106_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='codigo_ciudad_operadora_telefono',
            field=models.ForeignKey(default=21, to='bar.CodigoCiudadOperadoraTelefono'),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='codigo_pais_telefono',
            field=models.ForeignKey(default=595, to='bar.CodigoPaisTelefono'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 14, 21, 28, 890000, tzinfo=utc), help_text=b'Indique la fecha en la que el proveedor debe entregar el pedido.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 14, 21, 28, 890000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se realiza el pedido.'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='proveedor',
            field=models.CharField(help_text=b'Nombre del proveedor.', max_length=100),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='ruc',
            field=models.CharField(help_text=b'RUC del proveedor.', max_length=12),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefono',
            field=models.CharField(help_text=b'Ingrese el telefono del proveedor.', max_length=50),
        ),
    ]
