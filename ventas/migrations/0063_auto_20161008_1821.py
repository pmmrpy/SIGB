# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0062_venta_forma_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidodetalle',
            name='total_producto_pedido',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente tomando el Precio Venta del Producto por la Cantidad del Producto.', verbose_name=b'Total del Producto', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='venta',
            name='forma_pago',
            field=models.ForeignKey(verbose_name=b'Forma de Pago', to='bar.FormaPagoVenta', help_text=b'Seleccione la Forma de Pago.'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='numero_factura_venta',
            field=models.OneToOneField(related_name='numero_factura_venta', verbose_name=b'Numero de Factura de la Venta', to='bar.FacturaVenta', help_text=b'El Numero de Factura se asigna al momento de confirmarse la Venta.'),
        ),
    ]
