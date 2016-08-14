# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import compras.models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0085_auto_20160601_1205'),
        ('stock', '0066_auto_20160601_1205'),
        ('compras', '0003_proveedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_compra', models.DateTimeField(default=datetime.datetime(2016, 6, 1, 16, 5, 31, 931000, tzinfo=utc), help_text=b'La fecha y hora se asignan al momento de guardar los datos de la Compra. No se requiere el ingreso de este dato.')),
                ('total_compra', models.DecimalField(default=0, max_digits=20, decimal_places=2)),
                ('numero_factura', models.IntegerField(default=1, help_text=b'Ingrese el Numero de Factura que acompanha la Compra.', verbose_name=b'Numero de Factura de la Compra')),
                ('estado_compra', models.ForeignKey(default=1, to='bar.CompraEstado', help_text=b'El estado de compra se define de acuerdo a la Fecha de Entrega definida en la Orden de Compra.')),
            ],
            options={
                'verbose_name': 'Confirmacion de Compras',
            },
        ),
        migrations.CreateModel(
            name='CompraDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_producto', models.DecimalField(help_text=b'Ingrese la cantidad a adquirir del producto.', max_digits=10, decimal_places=2)),
                ('precio_compra_producto', models.DecimalField(help_text=b'Ingrese el precio de compra del producto definido por el proveedor.', max_digits=20, decimal_places=2)),
                ('compra', models.ForeignKey(related_name='compra', to='compras.Compra')),
            ],
            options={
                'verbose_name': 'Compra - Detalle',
                'verbose_name_plural': 'Compras - Detalles',
            },
        ),
        migrations.CreateModel(
            name='LineaCreditoProveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_linea_credito_proveedor', models.DateTimeField(default=datetime.datetime(2016, 6, 1, 16, 5, 31, 927000, tzinfo=utc), help_text=b'Ingrese la fecha en la quese registra la Linea deCredito ofrecida por el Proveedor.')),
                ('linea_credito_proveedor', models.IntegerField(help_text=b'Ingrese el monto ofrecido por el proveedor como Linea de Credito.')),
                ('estado_linea_credito_proveedor', models.BooleanField(help_text=b'')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_orden_compra', compras.models.SerialField(help_text=b'Este dato se genera automaticamente cada vez que se va crear una Orden de Compra.', unique=True, max_length=12, verbose_name=b'Numero de Orden de Compra')),
                ('fecha_orden_compra', models.DateTimeField(default=datetime.datetime(2016, 6, 1, 16, 5, 31, 929000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.')),
                ('fecha_entrega_orden_compra', models.DateTimeField(default=datetime.datetime(2016, 6, 2, 16, 5, 31, 929000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.')),
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
                ('ordencompra', models.ForeignKey(related_name='ordencompra', to='compras.OrdenCompra')),
            ],
            options={
                'verbose_name': 'Orden Compra - Detalle',
                'verbose_name_plural': 'Ordenes de Compras - Detalles',
            },
        ),
        migrations.CreateModel(
            name='ProductoProveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('producto', models.ForeignKey(to='stock.Producto')),
            ],
            options={
                'verbose_name': 'Producto por Proveedor',
                'verbose_name_plural': 'Productos por Proveedor',
            },
        ),
        migrations.CreateModel(
            name='TelefonoProveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telefono', models.IntegerField(help_text=b'Ingrese el telefono fijo o movil del proveedor. El dato debe contener solo numeros.')),
                ('interno', models.IntegerField(help_text=b'Ingrese el numero de interno.', null=True, blank=True)),
                ('contacto', models.CharField(help_text=b'Nombre de la persona a la cual contactar en este numero. (Hasta 100 caracteres)', max_length=100, null=True, blank=True)),
                ('codigo_ciudad_operadora_telefono', models.ForeignKey(default=21, to='bar.CodigoCiudadOperadoraTelefono', help_text=b'Seleccione o ingrese el codigo de ciudad u operadora de telefonia movil.')),
                ('codigo_pais_telefono', models.ForeignKey(default=595, to='bar.CodigoPaisTelefono')),
            ],
            options={
                'verbose_name': 'Proveedor - Telefono',
                'verbose_name_plural': 'Proveedores - Telefonos',
            },
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 1, 16, 5, 31, 926000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Proveedor. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
        migrations.AddField(
            model_name='telefonoproveedor',
            name='proveedor',
            field=models.ForeignKey(to='compras.Proveedor'),
        ),
        migrations.AddField(
            model_name='productoproveedor',
            name='proveedor',
            field=models.ForeignKey(to='compras.Proveedor'),
        ),
        migrations.AddField(
            model_name='ordencompradetalle',
            name='producto_orden_compra',
            field=models.ForeignKey(related_name='orden_compra_productos', to='compras.ProductoProveedor', help_text=b'Seleccione un producto a comprar.'),
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='proveedor_orden_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Proveedor', to='compras.Proveedor', help_text=b'Seleccione el Proveedor al cual se le realizara la Orden de Compra.'),
        ),
        migrations.AddField(
            model_name='lineacreditoproveedor',
            name='proveedor',
            field=models.ForeignKey(to='compras.Proveedor'),
        ),
        migrations.AddField(
            model_name='compradetalle',
            name='compra_producto',
            field=models.ForeignKey(related_name='compra_productos', default=1, to='compras.ProductoProveedor', help_text=b'Seleccione un producto a comprar.'),
        ),
        migrations.AddField(
            model_name='compra',
            name='numero_orden_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Numero de Orden de Compra', to='compras.OrdenCompra', help_text=b'Seleccione el Numero de Orden de Compra para la cual se confirmara la compra.'),
        ),
    ]
