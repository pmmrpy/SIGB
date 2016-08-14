# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0158_auto_20160706_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cajaestado',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Estado de la Caja. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion del Estado'),
        ),
        migrations.AlterField(
            model_name='categoriaproducto',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion de la Categoria de los productos. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion de la Categoria'),
        ),
        migrations.AlterField(
            model_name='compraestado',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Estado de la Compra. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion del Estado de la Compra'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 15, 2, 0, 275000, tzinfo=utc), help_text=b'Registra la fecha y hora en la que se definio la Cotizacion. Corresponde a la fecha y hora actual.', verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='deposito',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Deposito. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion del Deposito'),
        ),
        migrations.AlterField(
            model_name='mesaestado',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Estado de la Mesa. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion del Estado'),
        ),
        migrations.AlterField(
            model_name='ordencompraestado',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Estado de la Orden de Compra. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion del Estado de la Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='reservaestado',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Estado de la Reserva. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion del Estado'),
        ),
        migrations.AlterField(
            model_name='subcategoriaproducto',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion de la SubCategoria de los productos. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion de la SubCategoria'),
        ),
        migrations.AlterField(
            model_name='tipodeposito',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Tipo de Deposito. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion del Tipo de Deposito'),
        ),
        migrations.AlterField(
            model_name='tipoproducto',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Tipo de Producto. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion del Tipo de Producto'),
        ),
        migrations.AlterField(
            model_name='unidadmedidaproducto',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion de la Unidad de Medida. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion de la Unidad de Medida'),
        ),
    ]
