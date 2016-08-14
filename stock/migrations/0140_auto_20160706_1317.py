# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0160_auto_20160706_1317'),
        ('stock', '0139_auto_20160706_1102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='receta',
            options={'verbose_name': 'Productos Compuestos o Elaborados (Recetas)', 'verbose_name_plural': 'Productos Compuestos o Elaborados (Recetas)'},
        ),
        migrations.RemoveField(
            model_name='precioproducto',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='unidad_medida',
        ),
        migrations.AddField(
            model_name='precioproducto',
            name='fecha_precio_producto',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 17, 16, 59, 233000, tzinfo=utc), help_text=b'Ingrese la fecha y hora en la que se define el precio de venta del producto.'),
        ),
        migrations.AddField(
            model_name='producto',
            name='unidad_medida_comercializacion',
            field=models.ForeignKey(related_name='un_med_trading', default=1, to='bar.UnidadMedidaProducto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='unidad_medida_contenido',
            field=models.ForeignKey(related_name='un_med_contenido', default=1, to='bar.UnidadMedidaProducto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='contenido',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_alta_producto',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 17, 16, 59, 232000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Producto. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='fecha_hora_registro_stock',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 17, 16, 59, 236000, tzinfo=utc), help_text=b'Fecha y hora de registro'),
        ),
    ]
