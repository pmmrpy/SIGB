# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0262_auto_20160907_1712'),
        ('compras', '0178_auto_20160907_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='compradetalle',
            name='unidad_medida_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Unidad de Medida del Producto', to='bar.UnidadMedidaProducto', help_text=b'Debe ser la definida en los datos del Producto, no debe ser seleccionada por el usuario.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_compra',
            field=models.DateTimeField(help_text=b'La fecha y hora se asignan al momento de guardar los datos de la Compra. No se requiere el ingreso de este dato.', verbose_name=b'Fecha y hora Compra', auto_now=True),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='producto_compra',
            field=models.ForeignKey(related_name='compra_productos', verbose_name=b'Producto a Comprar', to='stock.Producto', help_text=b'Seleccione un producto a comprar.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 8, 21, 12, 24, 872000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
    ]
