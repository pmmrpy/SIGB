# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0276_auto_20160827_2010'),
        ('compras', '0219_auto_20161002_1505'),
        ('stock', '0204_productoventa'),
        ('bar', '0301_auto_20161002_1459'),
        ('ventas', '0052_auto_20161002_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comanda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area_encargada', models.CharField(max_length=3, verbose_name=b'Area Encargada', choices=[(b'COC', b'Cocina'), (b'BAR', b'Barra')])),
                ('fecha_hora_pedido_comanda', models.DateTimeField(verbose_name=b'Fecha/hora Pedido Comanda')),
                ('tiempo_estimado_elaboracion', models.TimeField(help_text=b'Corresponde al tiempo estimado que tomara elaborar el Producto Compuesto', verbose_name=b'Tiempo Estimado Elaboracion')),
                ('estado_comanda', models.CharField(max_length=3, verbose_name=b'Estado Comanda', choices=[(b'PEN', b'Pendiente'), (b'PRO', b'Procesada'), (b'CAN', b'Cancelada')])),
                ('fecha_hora_procesamiento_comanda', models.DateTimeField(null=True, verbose_name=b'Fecha/hora Procesamiento Comanda', blank=True)),
                ('numero_pedido', models.ForeignKey(to='ventas.Pedido')),
                ('producto_a_elaborar', models.ForeignKey(verbose_name=b'Producto a Elaborar', to='stock.ProductoCompuesto')),
            ],
            options={
                'verbose_name': 'Comanda',
                'verbose_name_plural': 'Comandas',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_hora_venta', models.DateTimeField(help_text=b'Registra la fecha y hora en la que se confirmo la Venta.', verbose_name=b'Fecha/hora de la Venta', auto_now_add=True)),
                ('forma_pago', models.CharField(help_text=b'Seleccione la Forma de Pago.', max_length=2, verbose_name=b'Forma de Pago', choices=[(b'CO', b'Contado'), (b'TC', b'Tarjeta de Credito'), (b'TD', b'Tarjeta de Debito'), (b'OM', b'Otros medios')])),
                ('total_venta', models.DecimalField(default=0, verbose_name=b'Total de la Venta', max_digits=18, decimal_places=0)),
                ('apertura_caja', models.ForeignKey(default=1, verbose_name=b'Apertura de Caja', to='ventas.AperturaCaja', help_text=b'Se asigna dependiendo del usuario logueado y de si posee una Apertura de Caja vigente.')),
                ('cliente_factura', models.ForeignKey(verbose_name=b'Cliente', to='clientes.Cliente', help_text=b'Corrobore con el Cliente si son correctos sus datos antes de confirmar la Venta.')),
                ('empresa', models.ForeignKey(default=9, to='compras.Empresa')),
                ('estado_venta', models.ForeignKey(default=1, verbose_name=b'Estado de la Venta', to='bar.VentaEstado', help_text=b'El estado de la Venta se establece de acuerdo a...')),
                ('numero_factura_venta', models.ForeignKey(related_name='numero_factura', default=1, verbose_name=b'Numero de Factura de la Venta', to='bar.FacturaVenta', help_text=b'El Numero de Factura se asigna al momento de confirmarse la Venta.')),
                ('numero_pedido', models.OneToOneField(verbose_name=b'Numero de Pedido', to='ventas.Pedido', help_text=b'Seleccione el Numero de Pedido para el cual se registrara la Venta.')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
        migrations.CreateModel(
            name='VentaDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio_producto_venta', models.DecimalField(help_text=b'El Precio de Venta del Producto se define en la pantalla de Productos.', verbose_name=b'Precio Venta Producto', max_digits=18, decimal_places=0)),
                ('cantidad_producto_venta', models.DecimalField(help_text=b'Ingrese la cantidad del producto solicitada por el Cliente.', verbose_name=b'Cantidad del Producto', max_digits=10, decimal_places=3)),
                ('total_producto_venta', models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente tomando el Precio de Venta del Producto por la Cantidad del Producto solicitada por el Cliente..', verbose_name=b'Total del Producto', max_digits=18, decimal_places=0)),
                ('producto_venta', models.ForeignKey(verbose_name=b'Producto', to='stock.ProductoVenta', help_text=b'Seleccione el Producto ordenado por el Cliente.')),
                ('venta', models.ForeignKey(to='ventas.Venta')),
            ],
            options={
                'verbose_name': 'Venta - Detalle',
                'verbose_name_plural': 'Ventas - Detalles',
            },
        ),
    ]
