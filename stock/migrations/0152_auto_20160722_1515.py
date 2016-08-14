# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0172_auto_20160722_1515'),
        ('stock', '0151_auto_20160722_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrecioVentaProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_precio_venta_producto', models.DateTimeField(default=datetime.datetime(2016, 7, 22, 19, 15, 15, 446000, tzinfo=utc), help_text=b'Ingrese la fecha y hora en la que se define el precio de venta del producto.')),
                ('precio_venta', models.DecimalField(help_text=b'Ingrese el precio de venta del producto.', max_digits=20, decimal_places=0)),
                ('activo', models.BooleanField(default=True, help_text=b'Indique si este precio es el que se encuentra activo actualmente. El producto puede tener un unico precio activo.')),
                ('producto', models.ForeignKey(to='stock.Producto')),
            ],
            options={
                'ordering': ('-fecha_precio_venta_producto',),
                'verbose_name': 'Producto - Precio de Venta',
                'verbose_name_plural': 'Productos - Precios de Venta',
            },
        ),
        migrations.CreateModel(
            name='ProductoCompuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('producto_compuesto', models.CharField(help_text=b'Ingrese el nombre o descripcion del Producto Compuesto o Elaborado.', max_length=100, verbose_name=b'Nombre del Producto Compuesto o Elaborado')),
                ('fecha_alta_producto_compuesto', models.DateTimeField(default=datetime.datetime(2016, 7, 22, 19, 15, 15, 446000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Producto. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta')),
                ('imagen', models.ImageField(default=1, upload_to=b'')),
                ('categoria', models.ForeignKey(to='bar.CategoriaProducto')),
                ('subcategoria', models.ForeignKey(to='bar.SubCategoriaProducto')),
                ('tipo_producto', models.ForeignKey(default=b"bar.TipoProducto.tipo_producto='VE'", to='bar.TipoProducto')),
            ],
            options={
                'verbose_name': 'Productos Compuestos o Elaborados (Recetas)',
                'verbose_name_plural': 'Productos Compuestos o Elaborados (Recetas)',
            },
        ),
        migrations.CreateModel(
            name='ProductoCompuestoDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_producto', models.DecimalField(help_text=b'Ingrese la cantidad del producto.', verbose_name=b'Cantidad Producto', max_digits=10, decimal_places=3)),
                ('producto', models.ForeignKey(verbose_name=b'Nombre del Producto', to='stock.Producto', help_text=b'Seleccione el o los Productos que componen este Producto Compuesto.')),
                ('producto_compuesto', models.ForeignKey(to='stock.ProductoCompuesto')),
            ],
            options={
                'verbose_name': 'Productos Compuestos o Elaborados (Recetas) - Detalles',
                'verbose_name_plural': 'Productos Compuestos o Elaborados (Recetas) - Detalles',
            },
        ),
        migrations.CreateModel(
            name='StockDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_hora_registro_stock', models.DateTimeField(default=datetime.datetime(2016, 7, 22, 19, 15, 15, 449000, tzinfo=utc), help_text=b'Fecha y hora de registro en el Stock.', verbose_name=b'Fecha y hora de registro')),
                ('tipo_movimiento', models.CharField(help_text=b'Seleccione el identificador del Tipo de Movimiento de Stock.', max_length=2, verbose_name=b'Tipo de Movimiento', choices=[(b'VE', b'Venta'), (b'CO', b'Compra'), (b'ME', b'Mermas'), (b'TR', b'Transferencias'), (b'DE', b'Devoluciones')])),
                ('cantidad_entrante', models.DecimalField(help_text=b'Cantidad entrante al Stock del producto.', verbose_name=b'Cantidad Entrante', max_digits=10, decimal_places=3)),
                ('cantidad_saliente', models.DecimalField(help_text=b'Cantidad saliente del Stock del producto.', verbose_name=b'Cantidad Saliente', max_digits=10, decimal_places=3)),
            ],
            options={
                'verbose_name': 'Detalle de Inventario de Productos',
                'verbose_name_plural': 'Detalles de Inventarios de Productos',
            },
        ),
        migrations.RemoveField(
            model_name='stock',
            name='cantidad_entrante',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='cantidad_saliente',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='fecha_hora_registro_stock',
        ),
        migrations.AddField(
            model_name='stockdetalle',
            name='stock',
            field=models.ForeignKey(to='stock.Stock'),
        ),
    ]
