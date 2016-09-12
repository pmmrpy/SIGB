# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0183_auto_20160909_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='disponible_linea_credito_proveedor',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente como la diferencia entre el Monto de la Linea de Credito y el Monto Utilizado de la Linea de Credito.', verbose_name=b'Monto Disponible Linea de Credito', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='cantidad_producto_compra',
            field=models.DecimalField(help_text=b'Ingrese la cantidad a adquirir del producto.', verbose_name=b'Cantidad Producto', max_digits=10, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='precio_producto_compra',
            field=models.DecimalField(help_text=b'Ingrese el precio de compra del producto definido por el proveedor.', verbose_name=b'Precio Compra', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='producto_compra',
            field=models.ForeignKey(related_name='compra_productos', verbose_name=b'Producto', to='stock.Producto', help_text=b'Seleccione un producto a comprar.'),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='total_producto_compra',
            field=models.DecimalField(default=0, verbose_name=b'Total Producto', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='unidad_medida_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Unidad de Medida Compra Producto', to='bar.UnidadMedidaProducto', help_text=b'Debe ser la definida en los datos del Producto, no debe ser seleccionada por el usuario.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 11, 21, 13, 1, 113000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
    ]
