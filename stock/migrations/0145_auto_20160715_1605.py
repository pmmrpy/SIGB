# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0165_auto_20160715_1605'),
        ('stock', '0144_auto_20160715_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stock_minimo', models.DecimalField(help_text=b'Cantidad minima del producto a mantener en Stock.', verbose_name=b'Stock Minimo', max_digits=10, decimal_places=3)),
                ('cantidad_existente', models.DecimalField(help_text=b'Cantidad existente en Stock', verbose_name=b'Cantidad Existente', max_digits=10, decimal_places=3)),
                ('cantidad_entrante', models.DecimalField(help_text=b'Cantidad entrante al stock del producto.', verbose_name=b'', max_digits=10, decimal_places=3)),
                ('cantidad_saliente', models.DecimalField(help_text=b'Cantidad saliente del stock del producto.', verbose_name=b'', max_digits=10, decimal_places=3)),
                ('fecha_hora_registro_stock', models.DateTimeField(default=datetime.datetime(2016, 7, 15, 20, 5, 37, 554000, tzinfo=utc), help_text=b'Fecha y hora de registro')),
            ],
            options={
                'verbose_name': 'Inventario de Productos',
                'verbose_name_plural': 'Inventario de Productos',
            },
        ),
        migrations.AlterField(
            model_name='precioproducto',
            name='fecha_precio_producto',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 15, 20, 5, 37, 553000, tzinfo=utc), help_text=b'Ingrese la fecha y hora en la que se define el precio de venta del producto.'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_alta_producto',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 15, 20, 5, 37, 552000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Producto. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
        migrations.AddField(
            model_name='stock',
            name='producto_stock',
            field=models.ForeignKey(related_name='producto_stock', to='stock.Producto'),
        ),
        migrations.AddField(
            model_name='stock',
            name='ubicacion',
            field=models.ForeignKey(to='bar.Deposito'),
        ),
        migrations.AlterUniqueTogether(
            name='stock',
            unique_together=set([('producto_stock', 'ubicacion')]),
        ),
    ]
