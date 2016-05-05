# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0025_compra'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompraDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_producto', models.DecimalField(help_text=b'Ingrese la cantidad a adquirir del producto.', max_digits=10, decimal_places=2)),
                ('precio_compra_producto', models.DecimalField(help_text=b'Ingrese el precio de compra del producto definido por el proveedor.', max_digits=20, decimal_places=2)),
                ('total_compra', models.DecimalField(default=0, max_digits=20, decimal_places=2)),
            ],
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 9, 1, 30, 0, 475000, tzinfo=utc), help_text=b'Indique la fecha en la que el proveedor debe entregar el pedido.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 9, 1, 30, 0, 475000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se realiza el pedido.'),
        ),
        migrations.AddField(
            model_name='compradetalle',
            name='compra',
            field=models.ForeignKey(related_name='compra', to='compras.Compra'),
        ),
        migrations.AddField(
            model_name='compradetalle',
            name='producto',
            field=models.ForeignKey(related_name='productos', to='compras.ProductoProveedor', help_text=b'Seleccione un producto a comprar.'),
        ),
    ]
