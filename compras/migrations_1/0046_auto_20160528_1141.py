# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0050_auto_20160528_1141'),
        ('compras', '0045_auto_20160524_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_orden_compra', models.IntegerField(default=999999999, help_text=b'Este dato se genera automaticamente cada vez que se va crear una Orden de Compra.', unique=True, verbose_name=b'Numero de Orden de Compra')),
                ('fecha_pedido', models.DateTimeField(default=datetime.datetime(2016, 5, 28, 15, 41, 39, 248000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.')),
                ('fecha_entrega', models.DateTimeField(default=datetime.datetime(2016, 5, 29, 15, 41, 39, 248000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar el pedido.')),
                ('total_orden_compra', models.DecimalField(default=0, max_digits=20, decimal_places=2)),
                ('forma_pago', models.ForeignKey(default=1, to='bar.FormaPagoCompra', help_text=b'Seleccione la Forma de Pago para esta compra.')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenCompraDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_producto', models.DecimalField(help_text=b'Ingrese la cantidad a adquirir del producto.', max_digits=10, decimal_places=2)),
                ('precio_orden_compra_producto', models.DecimalField(help_text=b'Ingrese el precio de compra del producto definidopor el proveedor.', max_digits=20, decimal_places=2)),
                ('numero_orden_compra', models.ForeignKey(related_name='ordencompra', to='compras.OrdenCompra')),
                ('orden_compra_producto', models.ForeignKey(related_name='orden_compra_productos', to='compras.ProductoProveedor', help_text=b'Seleccione un producto a comprar.')),
            ],
            options={
                'verbose_name': 'Orden Compra - Detalle',
                'verbose_name_plural': 'Ordenes de Compras - Detalles',
            },
        ),
        migrations.RemoveField(
            model_name='compra',
            name='fecha_entrega',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='fecha_pedido',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='forma_pago',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='numero_compra',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='proveedor_compra',
        ),
        migrations.RemoveField(
            model_name='compradetalle',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='compradetalle',
            name='total_compra',
        ),
        migrations.AddField(
            model_name='compra',
            name='estado_compra',
            field=models.ForeignKey(default=1, to='bar.CompraEstado', help_text=b'El estado de compra se define deacuerdo a la Fecha de Entregadefinida en la Orden de Compra.'),
        ),
        migrations.AddField(
            model_name='compra',
            name='fecha_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 28, 15, 41, 39, 250000, tzinfo=utc), help_text=b'La fecha y hora se asignan al momento de guardar los datos de la Compra. No se requiere el ingreso de este dato.'),
        ),
        migrations.AddField(
            model_name='compra',
            name='numero_factura',
            field=models.IntegerField(default=1, help_text=b'Ingrese el Numero de Factura que acompanha la Compra.', verbose_name=b'Numero de Factura de la Compra'),
        ),
        migrations.AddField(
            model_name='compra',
            name='total_compra',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=2),
        ),
        migrations.AddField(
            model_name='compradetalle',
            name='compra_producto',
            field=models.ForeignKey(related_name='compra_productos', default=1, to='compras.ProductoProveedor', help_text=b'Seleccione un producto a comprar.'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='fecha_linea_credito_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 28, 15, 41, 39, 245000, tzinfo=utc), help_text=b'Ingrese la fecha en la quese registra la Linea deCredito ofrecida por el Proveedor.'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='digito_verificador',
            field=models.IntegerField(default=1, help_text=b'Ingrese el digito verificador del RUC del Proveedor.'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='direccion',
            field=models.CharField(help_text=b'Ingrese la Direccion del Proveedor. (Hasta 200 caracteres)', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 28, 15, 41, 39, 244000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Proveedor. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='proveedor',
            field=models.CharField(help_text=b'Ingrese la Razon Social o el Nombre del Proveedor. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Razon Social o Nombre'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='ruc',
            field=models.CharField(help_text=b'Ingrese el RUC del Proveedor.', unique=True, max_length=15, verbose_name=b'RUC'),
        ),
        migrations.AlterField(
            model_name='telefonoproveedor',
            name='contacto',
            field=models.CharField(help_text=b'Nombre de la persona a la cual contactar en este numero. (Hasta 100 caracteres)', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='proveedor_compra',
            field=models.ForeignKey(verbose_name=b'Proveedor', to='compras.Proveedor', help_text=b'Seleccione el proveedor al cual se le realizara la compra.'),
        ),
        migrations.AddField(
            model_name='compra',
            name='numero_orden_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Numero de Orden de Compra', to='compras.OrdenCompra', help_text=b'Seleccione el Numero de Orden de Compra para la cual se confirmara la compra.'),
        ),
    ]
