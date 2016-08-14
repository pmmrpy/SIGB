# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0088_auto_20160620_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('producto_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='stock.Producto')),
                ('stock_minimo', models.DecimalField(help_text=b'Cantidad minima del producto a mantener en Stock.', verbose_name=b'Stock Minimo', max_digits=10, decimal_places=3)),
                ('cantidad_existente', models.DecimalField(help_text=b'Cantidad Existente en Stock', verbose_name=b'Cantidad Existente', max_digits=10, decimal_places=3)),
            ],
            bases=('stock.producto',),
        ),
        migrations.AddField(
            model_name='producto',
            name='fecha_alta_producto',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 22, 18, 14, 4, 175000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Producto. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
        migrations.AlterField(
            model_name='precioproducto',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 22, 18, 14, 4, 176000, tzinfo=utc), help_text=b'Ingrese la fecha y hora en la que se define el precio de venta del producto.'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='codigo_barra',
            field=models.CharField(help_text=b'', max_length=100, verbose_name=b'Codigo de Barra'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=models.CharField(help_text=b'', max_length=100, verbose_name=b'Marca'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='producto',
            field=models.CharField(help_text=b'Ingrese el nombre o descripcion del Producto.', max_length=100, verbose_name=b'Nombre del Producto'),
        ),
    ]
