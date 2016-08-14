# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0149_auto_20160722_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precioproducto',
            name='fecha_precio_producto',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 22, 15, 37, 59, 195000, tzinfo=utc), help_text=b'Ingrese la fecha y hora en la que se define el precio de venta del producto.'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='contenido',
            field=models.DecimalField(help_text=b'Ingrese el Contenido del producto de acuerdo a su Unidad de Medida.', verbose_name=b'Cantidad del Contenido', max_digits=10, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='producto',
            name='unidad_medida_compra',
            field=models.ForeignKey(related_name='un_med_compra', default=1, verbose_name=b'Unidad de Medida Compra', to='bar.UnidadMedidaProducto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='unidad_medida_contenido',
            field=models.ForeignKey(related_name='un_med_contenido', verbose_name=b'Unidad de Medida Contenido', to='bar.UnidadMedidaProducto'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='fecha_hora_registro_stock',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 22, 15, 37, 59, 196000, tzinfo=utc), help_text=b'Fecha y hora de registro en el Stock.', verbose_name=b'Fecha y hora de registro'),
        ),
    ]
