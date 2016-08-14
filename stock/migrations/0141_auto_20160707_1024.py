# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0140_auto_20160706_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receta',
            name='productos',
        ),
        migrations.RemoveField(
            model_name='recetadetalle',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='recetadetalle',
            name='receta',
        ),
        migrations.AlterField(
            model_name='precioproducto',
            name='fecha_precio_producto',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 7, 14, 24, 1, 852000, tzinfo=utc), help_text=b'Ingrese la fecha y hora en la que se define el precio de venta del producto.'),
        ),
        migrations.AlterField(
            model_name='precioproducto',
            name='precio_venta',
            field=models.DecimalField(help_text=b'Ingrese el precio de venta del producto.', max_digits=20, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_alta_producto',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 7, 14, 24, 1, 851000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Producto. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to=b'stock/productos/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=models.CharField(help_text=b'Ingrese la marca del Producto.', max_length=100, verbose_name=b'Marca'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='unidad_medida_comercializacion',
            field=models.ForeignKey(related_name='un_med_trading', verbose_name=b'Un. Med. Comerc.', to='bar.UnidadMedidaProducto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='unidad_medida_contenido',
            field=models.ForeignKey(related_name='un_med_contenido', verbose_name=b'Un. Med. Cont.', to='bar.UnidadMedidaProducto'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='fecha_hora_registro_stock',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 7, 14, 24, 1, 853000, tzinfo=utc), help_text=b'Fecha y hora de registro'),
        ),
        migrations.DeleteModel(
            name='Receta',
        ),
        migrations.DeleteModel(
            name='RecetaDetalle',
        ),
    ]
