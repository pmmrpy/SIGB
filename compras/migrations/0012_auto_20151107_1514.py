# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0014_auto_20151107_1514'),
        ('compras', '0011_auto_20151107_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='forma_pago',
            field=models.ForeignKey(default=1, to='bar.FormaPagoCompra', help_text=b'Seleccione la Forma de Pago para esta compra.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 18, 14, 12, 480000, tzinfo=utc), help_text=b'Indique la fecha en la que el proveedor debe entregar el pedido.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 18, 14, 12, 480000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se realiza el pedido.'),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='cantidad_producto',
            field=models.DecimalField(help_text=b'Ingrese la cantidad a adquirir del producto.', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='precio_compra_producto',
            field=models.DecimalField(help_text=b'Ingrese el precio de compra del producto definido por el proveedor.', max_digits=20, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='producto',
            field=models.ForeignKey(related_name='productos', to='compras.ProductoProveedor', help_text=b'Seleccione un producto a comprar.'),
        ),
    ]
