# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0157_auto_20160706_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cajaestado',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Estado de la Caja. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Descripcion del Estado'),
        ),
        migrations.AlterField(
            model_name='compraestado',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Estado de la Compra. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Descripcion del Estado de la Compra'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 14, 46, 43, 870000, tzinfo=utc), help_text=b'Registra la fecha y hora en la que se definio la Cotizacion. Corresponde a la fecha y hora actual.', verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='mesaestado',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Estado de la Mesa. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Descripcion del Estado'),
        ),
        migrations.AlterField(
            model_name='ordencompraestado',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Estado de la Orden de Compra. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Descripcion del Estado de la Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='reservaestado',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Estado de la Reserva. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Descripcion del Estado'),
        ),
        migrations.AlterField(
            model_name='unidadmedidaproducto',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion de la Unidad de Medida. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Descripcion de la Unidad de Medida'),
        ),
    ]
