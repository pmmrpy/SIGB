# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0025_auto_20160803_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='numero_pedido',
            field=models.ForeignKey(default=1, to='ventas.Pedido'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado_pedido',
            field=models.ForeignKey(default=1, verbose_name=b'Estado del Pedido', to='bar.PedidoEstado', help_text=b'El estado del Pedido se establece automaticamente.'),
        ),
        migrations.AlterField(
            model_name='pedidodetalle',
            name='cantidad_producto_pedido',
            field=models.DecimalField(default=1, help_text=b'Ingrese la cantidad del producto solicitado por el Cliente.', verbose_name=b'Cantidad del Producto', max_digits=10, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='pedidodetalle',
            name='precio_producto_pedido',
            field=models.ForeignKey(default=1, verbose_name=b'Precio Venta del Producto', to='stock.PrecioVentaProducto', help_text=b'El Precio de Venta se define de acuerdo al Producto seleccionado.'),
        ),
        migrations.AlterField(
            model_name='pedidodetalle',
            name='producto_pedido',
            field=models.ForeignKey(verbose_name=b'Producto a ordenar', to='stock.Producto', help_text=b'Seleccione el Producto ordenado por el Cliente.'),
        ),
        migrations.AlterField(
            model_name='pedidodetalle',
            name='total_producto_pedido',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente tomando el Precio Venta del Producto por la Cantidad del Producto.', verbose_name=b'Costo Total del Producto', max_digits=20, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='ventadetalle',
            name='producto_venta',
            field=models.ForeignKey(verbose_name=b'Producto', to='stock.Producto', help_text=b'Seleccione el Producto ordenado por el Cliente.'),
        ),
    ]
