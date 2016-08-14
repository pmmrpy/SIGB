# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0029_auto_20160809_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='mesa_pedido',
            field=models.ManyToManyField(help_text=b'Indique la/s mesa/s que sera/n ocupada/s por el/los Cliente/s.', to='bar.Mesa', verbose_name=b'Mesas disponibles'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='cliente',
            field=models.ForeignKey(help_text=b'Confirme con el Cliente si son correctos sus datos antes de confirmar la Venta.', to='clientes.Cliente'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='forma_pago',
            field=models.ForeignKey(help_text=b'Seleccione la Forma de Pago.', to='bar.FormaPagoVenta'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='numero_pedido',
            field=models.ForeignKey(verbose_name=b'Numero de Pedido', to='ventas.Pedido', help_text=b'Seleccione el Numero de Pedido para el cual se registrara la Venta.'),
        ),
        migrations.AlterField(
            model_name='ventadetalle',
            name='precio_producto_venta',
            field=models.ForeignKey(default=1, verbose_name=b'Precio de Venta del Producto', to='stock.PrecioVentaProducto', help_text=b'El Precio de Venta del Producto se asigna de acuerdo al Producto seleccionado.'),
        ),
        migrations.AlterField(
            model_name='ventadetalle',
            name='total_producto_venta',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente tomando el Precio de Venta del Producto por la Cantidad del Producto solicitada por el Cliente..', verbose_name=b'Total del Producto', max_digits=18, decimal_places=0),
        ),
    ]
