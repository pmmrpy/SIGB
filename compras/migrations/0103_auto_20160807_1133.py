# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0102_auto_20160804_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='numero_nota_credito_compra',
        ),
        migrations.RemoveField(
            model_name='compradetalle',
            name='unidad_medida_compra',
        ),
        migrations.AddField(
            model_name='compra',
            name='tipo_factura_compra',
            field=models.CharField(default=b'CON', max_length=3, verbose_name=b'Tipo de Factura', choices=[(b'CON', b'Contado'), (b'CRE', b'Credito')]),
        ),
        migrations.AddField(
            model_name='pagoproveedor',
            name='numero_comprobante_pago',
            field=models.IntegerField(default=1, help_text=b'Ingrese el Numero del Comprobante de Pago.', verbose_name=b'Numero de Comprobante de Pago'),
        ),
        migrations.AddField(
            model_name='pagoproveedor',
            name='numero_nota_credito',
            field=models.IntegerField(default=1, help_text=b'Ingrese el Numero de la Nota de Credito que anula o cancela la factura de la Compra en caso de que la misma se haya devuelto o cancelado.', verbose_name=b'Numero Nota de Credito'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='estado_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Estado de la Compra', to='bar.CompraEstado', help_text=b'La Compra puede tener 3 estados: PENDIENTE, CONFIRMADA o CANCELADA. El estado se asigna de forma automatica de acuerdo a la accion realizada.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_factura_compra',
            field=models.DateField(default=datetime.date(2016, 8, 7), help_text=b'Ingrese la fecha de la factura.', verbose_name=b'Fecha de la Factura de la Compra'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='numero_factura_compra',
            field=models.IntegerField(help_text=b'Ingrese el Numero de Factura que acompana la Compra.', verbose_name=b'Numero de Factura de la Compra'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='total_compra',
            field=models.DecimalField(default=0, help_text=b'Este campo se calcula en funcion al detalle de la Compra.', verbose_name=b'Total de la Compra', max_digits=18, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='cantidad_producto_compra',
            field=models.DecimalField(help_text=b'Ingrese la cantidad a adquirir del producto.', verbose_name=b'Cantidad del Producto a Comprar', max_digits=10, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='precio_producto_compra',
            field=models.DecimalField(help_text=b'Ingrese el precio de compra del producto definido por el proveedor.', verbose_name=b'Precio de Compra Producto', max_digits=20, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='producto_compra',
            field=models.ForeignKey(related_name='compra_productos', default=1, verbose_name=b'Producto a Comprar', to='compras.ProductoProveedor', help_text=b'Seleccione un producto a comprar.'),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='total_producto_compra',
            field=models.DecimalField(default=0, verbose_name=b'Total del Producto a Comprar', max_digits=20, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 8, 15, 33, 15, 619000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 7, 15, 33, 15, 619000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de la Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='productoproveedor',
            name='producto',
            field=models.ForeignKey(help_text=b'Seleccione el Producto a relacionar con el Proveedor.', to='stock.Producto'),
        ),
        migrations.AlterField(
            model_name='productoproveedor',
            name='proveedor',
            field=models.ForeignKey(help_text=b'Seleccione el Proveedor al cual asignar un Producto.', to='compras.Proveedor'),
        ),
    ]
