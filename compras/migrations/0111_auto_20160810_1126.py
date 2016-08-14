# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0194_auto_20160810_1126'),
        ('compras', '0110_auto_20160809_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaProveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_factura_compra', models.IntegerField(help_text=b'Ingrese el Numero de Factura que acompana la Compra.', verbose_name=b'Numero de Factura de la Compra')),
                ('fecha_factura_compra', models.DateField(default=datetime.date(2016, 8, 10), help_text=b'Ingrese la fecha de la Factura.', verbose_name=b'Fecha de la Factura de la Compra')),
                ('plazo_factura_compra', models.PositiveIntegerField(help_text=b'En caso de Credito establecer el plazo de tiempo en dias para el pago.', verbose_name=b'Plazo de Pago Compra')),
                ('total_pago_factura', models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente en funcion a los pagos registrados para la Factura.', verbose_name=b'Total pagado de la Factura', max_digits=18, decimal_places=0)),
            ],
            options={
                'verbose_name': 'Proveedor - Factura',
                'verbose_name_plural': 'Proveedores - Facturas',
            },
        ),
        migrations.RemoveField(
            model_name='pagoproveedor',
            name='compra',
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_factura_compra',
            field=models.DateField(default=datetime.date(2016, 8, 10), help_text=b'Ingrese la fecha de la factura.', verbose_name=b'Fecha de la Factura de la Compra'),
        ),
        # migrations.AlterField(
        #     model_name='compra',
        #     name='tipo_factura_compra',
        #     field=models.ForeignKey(verbose_name=b'Tipo de Factura', to='bar.TipoFacturaCompra', help_text=b'Seleccione el Tipo de Factura para la Compra.'),
        # ),
        migrations.AlterField(
            model_name='compra',
            name='total_compra',
            field=models.DecimalField(default=0, help_text=b'Este campo se calcula en funcion al detalle de la Compra.', verbose_name=b'Total de la Compra', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='precio_producto_compra',
            field=models.DecimalField(help_text=b'Ingrese el precio de compra del producto definido por el proveedor.', verbose_name=b'Precio de Compra Producto', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='total_producto_compra',
            field=models.DecimalField(default=0, verbose_name=b'Total del Producto a Comprar', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 11, 15, 26, 49, 365000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 10, 15, 26, 49, 365000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de la Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='total_orden_compra',
            field=models.DecimalField(default=0, verbose_name=b'Total de la Orden de Compra', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='ordencompradetalle',
            name='precio_producto_orden_compra',
            field=models.DecimalField(help_text=b'Ingrese el precio de compra del producto definido por el proveedor.', verbose_name=b'Precio del Producto', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='ordencompradetalle',
            name='total_producto_orden_compra',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente tomando el Precio del Producto por la Cantidad del Producto.', verbose_name=b'Total del Producto', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='pagoproveedor',
            name='fecha_pago_proveedor',
            field=models.DateField(help_text=b'La fecha y hora del Pago al Proveedor se asignan al momento de guardar los datos del Pago. No se requiere el ingreso de este dato.', verbose_name=b'Fecha/Hora Pago Proveedor'),
        ),
        migrations.AddField(
            model_name='facturaproveedor',
            name='compra',
            field=models.ForeignKey(verbose_name=b'Compra Asociada', to='compras.Compra', help_text=b'Seleccione la Compra cuya Factura sera registrada.'),
        ),
        migrations.AddField(
            model_name='facturaproveedor',
            name='forma_pago_compra',
            field=models.ForeignKey(verbose_name=b'Forma de Pago Compra', to='bar.FormaPagoCompra', help_text=b'Seleccione la Forma de Pago para esta Factura.'),
        ),
        migrations.AddField(
            model_name='facturaproveedor',
            name='tipo_factura_compra',
            field=models.ForeignKey(verbose_name=b'Tipo de Factura Compra', to='bar.TipoFacturaCompra', help_text=b'Seleccione el Tipo de Factura.'),
        ),
        migrations.AddField(
            model_name='pagoproveedor',
            name='factura_proveedor',
            field=models.ForeignKey(default=1, verbose_name=b'Factura Proveedor', to='compras.FacturaProveedor', help_text=b'Seleccione la Factura a la cual se aplicara el Pago.'),
        ),
    ]
