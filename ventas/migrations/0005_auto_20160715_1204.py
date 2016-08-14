# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0163_auto_20160715_1204'),
        ('clientes', '0187_auto_20160715_1204'),
        ('compras', '0080_auto_20160715_1204'),
        ('stock', '0143_auto_20160715_1204'),
        ('personal', '0183_auto_20160715_1204'),
        ('ventas', '0004_auto_20160518_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='AperturaCaja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_hora_apertura_caja', models.DateTimeField()),
                ('monto_apertura', models.DecimalField(default=0, help_text=b'', verbose_name=b'', max_digits=20, decimal_places=0)),
                ('caja', models.ForeignKey(to='bar.Caja')),
                ('cajero', models.ForeignKey(to='personal.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Cocina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_venta', models.DateTimeField(default=datetime.datetime(2016, 7, 15, 16, 4, 7, 785000, tzinfo=utc))),
                ('total_venta', models.DecimalField(default=0, verbose_name=b'Total de la Venta', max_digits=20, decimal_places=0)),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
                ('empresa', models.ForeignKey(to='compras.Empresa')),
                ('estado_venta', models.ForeignKey(default=1, verbose_name=b'Estado de la Venta', to='bar.VentaEstado', help_text=b'El estado de la Venta se establece de acuerdo a...')),
                ('forma_pago', models.ForeignKey(to='bar.FormaPagoVenta')),
                ('reserva', models.ForeignKey(to='clientes.Reserva')),
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
                ('cantidad_producto_venta', models.DecimalField(help_text=b'Ingrese la cantidad del producto solicitada por el Cliente.', verbose_name=b'Cantidad del Producto', max_digits=10, decimal_places=3)),
                ('total_producto_venta', models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente tomando el Precio del Producto por la Cantidad del Producto.', verbose_name=b'Total del Producto ordenado por el Cliente.', max_digits=20, decimal_places=0)),
                ('precio_producto_venta', models.ForeignKey(to='stock.PrecioProducto')),
                ('producto_venta', models.ForeignKey(to='stock.Producto')),
                ('venta', models.ForeignKey(to='ventas.Venta')),
            ],
            options={
                'verbose_name': 'Venta - Detalle',
                'verbose_name_plural': 'Ventas - Detalles',
            },
        ),
        migrations.AlterModelOptions(
            name='pedido',
            options={'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='mesa',
            new_name='mesa_pedido',
        ),
        migrations.RenameField(
            model_name='pedidodetalle',
            old_name='producto',
            new_name='producto_pedido',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='pedidodetalle',
            name='cantidad_producto',
        ),
        migrations.AddField(
            model_name='pedido',
            name='estado_pedido',
            field=models.ForeignKey(default=1, verbose_name=b'Estado del Pedido', to='bar.PedidoEstado', help_text=b'El estado del Pedido se establece automaticamente de acuerdo a...'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 15, 16, 4, 7, 783000, tzinfo=utc), help_text=b'', verbose_name=b''),
        ),
        migrations.AddField(
            model_name='pedido',
            name='mozo_pedido',
            field=models.ForeignKey(default=3, to='personal.Empleado'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='total_pedido',
            field=models.DecimalField(default=0, verbose_name=b'Total del Pedido', max_digits=20, decimal_places=0),
        ),
        migrations.AddField(
            model_name='pedidodetalle',
            name='cantidad_producto_pedido',
            field=models.DecimalField(default=1, help_text=b'Ingrese la cantidad del producto solicitada por el Cliente.', verbose_name=b'Cantidad del Producto', max_digits=10, decimal_places=3),
        ),
        migrations.AddField(
            model_name='pedidodetalle',
            name='fecha_pedido_detalle',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 15, 16, 4, 7, 784000, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='pedidodetalle',
            name='precio_producto_pedido',
            field=models.ForeignKey(default=1, to='stock.PrecioProducto'),
        ),
        migrations.AddField(
            model_name='pedidodetalle',
            name='total_producto_pedido',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente tomando el Precio del Producto por la Cantidad del Producto.', verbose_name=b'Total del Producto ordenado por el Cliente.', max_digits=20, decimal_places=0),
        ),
    ]
