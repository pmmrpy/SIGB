# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0142_auto_20160704_1112'),
        ('compras', '0058_auto_20160704_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('numero_compra', models.AutoField(help_text=b'Este dato se genera automaticamente cada vez que se va a confirmar una Compra.', serialize=False, verbose_name=b'ID de Compra', primary_key=True)),
                ('fecha_compra', models.DateTimeField(default=datetime.datetime(2016, 7, 4, 15, 12, 29, 958000, tzinfo=utc), help_text=b'La fecha y hora se asignan al momento de guardar los datos de la Compra. No se requiere el ingreso de este dato.', verbose_name=b'Fecha y hora de la Compra')),
                ('total_compra', models.DecimalField(default=0, max_digits=20, decimal_places=2)),
                ('numero_factura_compra', models.IntegerField(default=1, help_text=b'Ingrese el Numero de Factura que acompana la Compra.', verbose_name=b'Numero de Factura de la Compra')),
                ('fecha_factura_compra', models.DateField(default=datetime.datetime(2016, 7, 4, 15, 12, 29, 959000, tzinfo=utc), help_text=b'Ingrese la fecha de la factura.', verbose_name=b'Fecha de la Factura de la Compra')),
                ('numero_nota_credito_compra', models.IntegerField(default=1, help_text=b'Ingrese el Numero de la Nota de Credito que acompana la Compra en caso de que la Forma de Pago de la misma sea a Credito.', verbose_name=b'Numero Nota de Credito')),
                ('estado_compra', models.ForeignKey(default=1, to='bar.CompraEstado', help_text=b'La Compra solo puede tener 2 estados: CONFIRMADA o CANCELADA.')),
            ],
            options={
                'verbose_name': 'Confirmacion de Compra',
                'verbose_name_plural': 'Confirmaciones de Compras',
            },
        ),
        migrations.CreateModel(
            name='CompraDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio_producto_compra', models.DecimalField(help_text=b'Ingrese el precio de compra del producto definido por el proveedor.', max_digits=20, decimal_places=2)),
                ('cantidad_producto_compra', models.DecimalField(help_text=b'Ingrese la cantidad a adquirir del producto.', max_digits=10, decimal_places=3)),
                ('total_producto_compra', models.DecimalField(default=0, max_digits=20, decimal_places=2)),
                ('numero_compra', models.ForeignKey(to='compras.Compra')),
                ('producto_compra', models.ForeignKey(related_name='compra_productos', default=1, to='compras.ProductoProveedor', help_text=b'Seleccione un producto a comprar.')),
            ],
            options={
                'verbose_name': 'Compra - Detalle',
                'verbose_name_plural': 'Compras - Detalles',
            },
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='fecha_linea_credito_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 4, 15, 12, 29, 955000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se registra la Linea de Credito ofrecida por el Proveedor.', verbose_name=b'Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 5, 15, 12, 29, 957000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 4, 15, 12, 29, 957000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de la Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 4, 15, 12, 29, 954000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Proveedor. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
        migrations.AddField(
            model_name='compra',
            name='numero_orden_compra',
            field=models.ForeignKey(verbose_name=b'Numero de Orden de Compra', to='compras.OrdenCompra', help_text=b'Seleccione el Numero de Orden de Compra para la cual se confirmara la Compra.'),
        ),
    ]
