# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0049_auto_20160930_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='estado_pedido',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='mesa_pedido',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='mozo_pedido',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='reserva',
        ),
        migrations.RemoveField(
            model_name='pedidodetalle',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='pedidodetalle',
            name='producto_pedido',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='entrega_reserva',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='numero_pedido',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='posee_reserva',
        ),
        migrations.AlterField(
            model_name='venta',
            name='cliente_factura',
            field=models.ForeignKey(verbose_name=b'Cliente', to='clientes.Cliente', help_text=b'Corrobore con el Cliente si son correctos sus datos antes de confirmar la Venta.'),
        ),
        migrations.AlterField(
            model_name='ventadetalle',
            name='producto_venta',
            field=models.ForeignKey(verbose_name=b'Producto', to='stock.ProductoVenta', help_text=b'Seleccione el Producto ordenado por el Cliente.'),
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
        migrations.DeleteModel(
            name='PedidoDetalle',
        ),
    ]
