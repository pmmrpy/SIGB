# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0126_auto_20160704_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precioproducto',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 5, 21, 50, 2, 644000, tzinfo=utc), help_text=b'Ingrese la fecha y hora en la que se define el precio de venta del producto.'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='codigo_barra',
            field=models.CharField(help_text=b'Ingrese el codigo de barra del Producto si posee.', max_length=100, verbose_name=b'Codigo de Barra'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_alta_producto',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 5, 21, 50, 2, 643000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Producto. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='subcategoria',
            field=models.ForeignKey(to='bar.SubCategoriaProducto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo_producto',
            field=models.ForeignKey(to='bar.TipoProducto'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='fecha_hora_registro_stock',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 5, 21, 50, 2, 647000, tzinfo=utc), help_text=b'Fecha y hora de registro'),
        ),
    ]
