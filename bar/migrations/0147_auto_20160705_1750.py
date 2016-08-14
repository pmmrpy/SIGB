# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0146_auto_20160704_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caja',
            name='numero',
        ),
        migrations.RemoveField(
            model_name='cajaubicacion',
            name='ubicacion',
        ),
        migrations.RemoveField(
            model_name='mesa',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='mesaubicacion',
            name='ubicacion',
        ),
        migrations.AddField(
            model_name='caja',
            name='numero_caja',
            field=models.PositiveIntegerField(default=1, help_text=b'Ingrese el Numero de Caja.', verbose_name=b'Numero de Caja'),
        ),
        migrations.AddField(
            model_name='cajaubicacion',
            name='caja_ubicacion',
            field=models.CharField(default=1, help_text=b'Ingrese un nombre o identificador de la ubicacion de la Caja. (Hasta 30 caracteres)', max_length=30, verbose_name=b'Ubicacion de la Caja'),
        ),
        migrations.AddField(
            model_name='mesa',
            name='nombre_mesa',
            field=models.CharField(default=b'Mesa', help_text=b'Ingrese el nombre o descripcion de la Mesa. (Hasta 20 caracteres)', max_length=20, verbose_name=b'Mesa'),
        ),
        migrations.AddField(
            model_name='mesa',
            name='numero_mesa',
            field=models.PositiveIntegerField(default=1, help_text=b'Ingrese el Numero de Mesa.', verbose_name=b'Numero de Mesa'),
        ),
        migrations.AddField(
            model_name='mesaubicacion',
            name='mesa_ubicacion',
            field=models.CharField(default=1, help_text=b'Ingrese un nombre o identificador de la ubicacion de la Mesa. (Hasta 30 caracteres)', max_length=30, verbose_name=b'Ubicacion de la Mesa'),
        ),
        migrations.AlterField(
            model_name='cajaestado',
            name='caja_estado',
            field=models.CharField(help_text=b'Ingrese el identificador del Estado de la Caja. (Hasta 3 caracteres', max_length=3, verbose_name=b'Estado de la Caja'),
        ),
        migrations.AlterField(
            model_name='cajaestado',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Estado de la Caja.', max_length=50, verbose_name=b'Descripcion del Estado'),
        ),
        migrations.AlterField(
            model_name='cajaubicacion',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion de la Ubicacion de la Caja. (Hasta 50 caracteres)', max_length=50, verbose_name=b'Descripcion de la Ubicacion'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 5, 21, 50, 2, 608000, tzinfo=utc), help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual.'),
        ),
        migrations.AlterField(
            model_name='documento',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Tipo de Documento. (Hasta 50 caracteres)', max_length=50, verbose_name=b'Descripcion del Tipo de Documento'),
        ),
        migrations.AlterField(
            model_name='documento',
            name='documento',
            field=models.CharField(help_text=b'Ingrese el identificador del Tipo de Documento. (Hasta 3 caracteres)', max_length=3, verbose_name=b'Identificador Tipo de Documento'),
        ),
        migrations.AlterField(
            model_name='formapagocompra',
            name='forma_pago_compra',
            field=models.CharField(max_length=2, choices=[(b'CO', b'Contado'), (b'CR', b'Credito')]),
        ),
        migrations.AlterField(
            model_name='formapagocompra',
            name='plazo_compra',
            field=models.PositiveIntegerField(help_text=b'En caso de Credito establecer el plazo de tiempo en d\xc3\xadas para el pago.'),
        ),
        migrations.AlterField(
            model_name='formapagoventa',
            name='forma_pago_venta',
            field=models.CharField(max_length=2, choices=[(b'CO', b'Contado'), (b'TC', b'Tarjeta de Credito'), (b'TD', b'Tarjeta de Debito')]),
        ),
        migrations.AlterField(
            model_name='mesaestado',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Estado de la Mesa.', max_length=50, verbose_name=b'Descripcion del Estado'),
        ),
        migrations.AlterField(
            model_name='mesaestado',
            name='mesa_estado',
            field=models.CharField(help_text=b'Ingrese el identificador del Estado de la Mesa. (Hasta 3 caracteres)', max_length=3, verbose_name=b'Estado de la Mesa'),
        ),
        migrations.AlterField(
            model_name='mesaubicacion',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion de la Ubicacion de la Mesa. (Hasta 50 caracteres)', max_length=50, verbose_name=b'Descripcion de la Ubicacion'),
        ),
        migrations.AlterField(
            model_name='reservaestado',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Estado de la Reserva. (Hasta 50 caracteres)', max_length=50, verbose_name=b'Descripcion del Estado'),
        ),
        migrations.AlterField(
            model_name='reservaestado',
            name='reserva_estado',
            field=models.CharField(help_text=b'Ingrese el identificador del Estado de la Reserva. (Hasta 1 caracter)', max_length=1, verbose_name=b'Estado de la Reserva'),
        ),
        migrations.AlterField(
            model_name='subcategoriaproducto',
            name='categoria',
            field=models.ForeignKey(to='bar.CategoriaProducto'),
        ),
    ]
