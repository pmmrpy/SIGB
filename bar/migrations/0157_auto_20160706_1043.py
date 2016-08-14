# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0156_auto_20160706_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='cajaestado',
            name='descripcion',
            field=models.CharField(default=b'Borrar', help_text=b'Ingrese la descripcion del Estado de la Caja. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Descripcion del Estado'),
        ),
        migrations.AddField(
            model_name='compraestado',
            name='descripcion',
            field=models.CharField(default=b'Borrar', help_text=b'Ingrese la descripcion del Estado de la Compra. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Descripcion del Estado de la Compra'),
        ),
        migrations.AddField(
            model_name='mesaestado',
            name='descripcion',
            field=models.CharField(default=b'Borrar', help_text=b'Ingrese la descripcion del Estado de la Mesa. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Descripcion del Estado'),
        ),
        migrations.AddField(
            model_name='ordencompraestado',
            name='descripcion',
            field=models.CharField(default=b'Borrar', help_text=b'Ingrese la descripcion del Estado de la Orden de Compra. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Descripcion del Estado de la Orden de Compra'),
        ),
        migrations.AddField(
            model_name='reservaestado',
            name='descripcion',
            field=models.CharField(default=b'Borrar', help_text=b'Ingrese la descripcion del Estado de la Reserva. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Descripcion del Estado'),
        ),
        migrations.AddField(
            model_name='unidadmedidaproducto',
            name='descripcion',
            field=models.CharField(default=b'Borrar', help_text=b'Ingrese la descripcion de la Unidad de Medida. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Descripcion de la Unidad de Medida'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 14, 43, 39, 446000, tzinfo=utc), help_text=b'Registra la fecha y hora en la que se definio la Cotizacion. Corresponde a la fecha y hora actual.', verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='tipoproducto',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Tipo de Producto. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Descripcion del Tipo de Producto'),
        ),
        migrations.AlterField(
            model_name='tipoproducto',
            name='tipo_producto',
            field=models.CharField(help_text=b'Ingrese el identificador del Tipo de Producto. (Hasta 2 caracteres)', max_length=2, verbose_name=b'Tipo de Producto'),
        ),
    ]
