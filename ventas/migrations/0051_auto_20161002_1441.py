# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0300_auto_20161002_1441'),
        ('clientes', '0276_auto_20160827_2010'),
        ('personal', '0272_auto_20160827_2010'),
        ('stock', '0204_productoventa'),
        ('ventas', '0050_auto_20161002_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('numero_pedido', models.AutoField(help_text=b'Este dato se genera automaticamente cada vez que se va crear un Pedido.', serialize=False, verbose_name=b'Nro. Pedido', primary_key=True)),
                ('fecha_pedido', models.DateTimeField(help_text=b'La fecha y hora del Pedido se asignara automaticamente una vez que sea guardado.', verbose_name=b'Fecha/Hora del Pedido', auto_now_add=True)),
                ('total_pedido', models.DecimalField(default=0, verbose_name=b'Total del Pedido', max_digits=18, decimal_places=0)),
                ('estado_pedido', models.ForeignKey(default=1, verbose_name=b'Estado del Pedido', to='bar.PedidoEstado', help_text=b'El estado del Pedido se establece automaticamente.')),
                ('mesa_pedido', models.ManyToManyField(help_text=b'Indique la/s mesa/s que sera/n ocupada/s por el/los Cliente/s.', to='bar.Mesa', verbose_name=b'Mesas disponibles')),
                ('mozo_pedido', models.ForeignKey(verbose_name=b'Atendido por?', to_field=b'usuario', to='personal.Empleado', help_text=b'Este dato se completara automaticamente cuando el Pedido sea guardado.')),
                ('reserva', models.ForeignKey(blank=True, to='clientes.Reserva', help_text=b'Seleccione una Reserva en caso de que el Cliente haya realizado una.', null=True)),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='PedidoDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio_producto_pedido', models.DecimalField(help_text=b'El Precio de Venta del Producto se define en la pantalla de Productos.', verbose_name=b'Precio Venta Producto', max_digits=18, decimal_places=0)),
                ('cantidad_producto_pedido', models.DecimalField(default=1, help_text=b'Ingrese la cantidad del producto solicitado por el Cliente.', verbose_name=b'Cantidad del Producto', max_digits=10, decimal_places=3)),
                ('total_producto_pedido', models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente tomando el Precio Venta del Producto por la Cantidad del Producto.', verbose_name=b'Costo Total del Producto', max_digits=18, decimal_places=0)),
                ('fecha_pedido_detalle', models.DateTimeField(help_text=b'Registra la fecha y hora en que se realizo el detalle del Pedido, util cuando el cliente pide mas productos.', verbose_name=b'Fecha/hora del detalle del Pedido', auto_now_add=True)),
                ('pedido', models.ForeignKey(to='ventas.Pedido')),
                ('producto_pedido', models.ForeignKey(verbose_name=b'Producto a ordenar', to='stock.ProductoVenta', help_text=b'Seleccione el Producto ordenado por el Cliente.')),
            ],
            options={
                'verbose_name': 'Pedido - Detalle',
                'verbose_name_plural': 'Pedidos - Detalles',
            },
        ),
        # migrations.AddField(
        #     model_name='comanda',
        #     name='numero_pedido',
        #     field=models.ForeignKey(default=0, to='ventas.Pedido'),
        # ),
        # migrations.AddField(
        #     model_name='venta',
        #     name='numero_pedido',
        #     field=models.OneToOneField(default=0, to='ventas.Pedido', help_text=b'Seleccione el Numero de Pedido para el cual se registrara la Venta.', verbose_name=b'Numero de Pedido'),
        # ),
    ]
