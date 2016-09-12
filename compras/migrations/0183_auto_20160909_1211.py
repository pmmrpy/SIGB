# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0266_auto_20160909_1211'),
        ('compras', '0182_auto_20160909_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='compradetalle',
            name='unidad_medida_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Unidad de Medida del Producto', to='bar.UnidadMedidaProducto', help_text=b'Debe ser la definida en los datos del Producto, no debe ser seleccionada por el usuario.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 10, 16, 10, 57, 893000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
    ]
