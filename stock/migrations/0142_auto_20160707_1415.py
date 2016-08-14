# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0162_auto_20160707_1415'),
        ('stock', '0141_auto_20160707_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='unidad_medida_comercializacion',
        ),
        migrations.AddField(
            model_name='producto',
            name='unidad_medida_compra',
            field=models.ForeignKey(related_name='un_med_trading', default=1, verbose_name=b'Unidad Medida Compra', to='bar.UnidadMedidaProducto'),
        ),
        migrations.AlterField(
            model_name='precioproducto',
            name='fecha_precio_producto',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 7, 18, 15, 10, 582000, tzinfo=utc), help_text=b'Ingrese la fecha y hora en la que se define el precio de venta del producto.'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_alta_producto',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 7, 18, 15, 10, 581000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Producto. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='unidad_medida_contenido',
            field=models.ForeignKey(related_name='un_med_contenido', verbose_name=b'Unidad Medida Contenido', to='bar.UnidadMedidaProducto'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='fecha_hora_registro_stock',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 7, 18, 15, 10, 583000, tzinfo=utc), help_text=b'Fecha y hora de registro'),
        ),
    ]
