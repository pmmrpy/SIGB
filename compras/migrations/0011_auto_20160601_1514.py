# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0093_auto_20160601_1514'),
        ('compras', '0010_auto_20160601_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('numero_orden_compra', models.AutoField(help_text=b'Este dato se genera automaticamente cada vez que se va crear una Orden de Compra.', serialize=False, verbose_name=b'Numero de Orden de Compra', primary_key=True)),
                ('fecha_orden_compra', models.DateTimeField(default=datetime.datetime(2016, 6, 1, 19, 14, 4, 975000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.')),
                ('fecha_entrega_orden_compra', models.DateTimeField(default=datetime.datetime(2016, 6, 2, 19, 14, 4, 975000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.')),
                ('total_orden_compra', models.DecimalField(default=0, max_digits=20, decimal_places=2)),
                ('estado_orden_compra', models.ForeignKey(default=1, to='bar.OrdenCompraEstado', help_text=b'El estado de la Orden de Compra se define de acuerdo a la Fecha de Entrega definida.')),
                ('forma_pago_orden_compra', models.ForeignKey(default=1, to='bar.FormaPagoCompra', help_text=b'Seleccione la Forma de Pago para esta Orden de Compra.')),
            ],
            options={
                'verbose_name': 'Orden de Compra',
                'verbose_name_plural': 'Ordenes de Compra',
            },
        ),
        migrations.CreateModel(
            name='OrdenCompraDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio_producto_orden_compra', models.DecimalField(help_text=b'Ingrese el precio de compra del producto definidopor el proveedor.', max_digits=20, decimal_places=2)),
                ('cantidad_producto_orden_compra', models.DecimalField(help_text=b'Ingrese la cantidad a adquirir del producto.', max_digits=10, decimal_places=2)),
                ('total_producto_orden_compra', models.DecimalField(default=0, max_digits=20, decimal_places=2)),
                ('numero_orden_compra', models.ForeignKey(related_name='ordencompra', to='compras.OrdenCompra')),
                ('producto_orden_compra', models.ForeignKey(related_name='orden_compra_productos', to='compras.ProductoProveedor', help_text=b'Seleccione un producto a comprar.')),
            ],
            options={
                'verbose_name': 'Orden Compra - Detalle',
                'verbose_name_plural': 'Ordenes de Compras - Detalles',
            },
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 1, 19, 14, 4, 976000, tzinfo=utc), help_text=b'La fecha y hora se asignan al momento de guardar los datos de la Compra. No se requiere el ingreso de este dato.'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='fecha_linea_credito_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 1, 19, 14, 4, 973000, tzinfo=utc), help_text=b'Ingrese la fecha en la quese registra la Linea deCredito ofrecida por el Proveedor.'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 1, 19, 14, 4, 972000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Proveedor. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='proveedor_orden_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Proveedor', to='compras.Proveedor', help_text=b'Seleccione el Proveedor al cual se le realizara la Orden de Compra.'),
        ),
        migrations.AddField(
            model_name='compra',
            name='numero_orden_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Numero de Orden de Compra', to='compras.OrdenCompra', help_text=b'Seleccione el Numero de Orden de Compra para la cual se confirmara la compra.'),
        ),
    ]
