# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0152_auto_20160706_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cajaubicacion',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion de la Ubicacion de la Caja. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Descripcion de la Ubicacion'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 4, 57, 55, 844000, tzinfo=utc), help_text=b'Registra la fecha y hora en la que se definio la Cotizacion. Corresponde a la fecha y hora actual.', verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='formapagocompra',
            name='forma_pago_compra',
            field=models.CharField(max_length=2, verbose_name=b'Forma de Pago Compra', choices=[(b'CO', b'Contado'), (b'CR', b'Credito')]),
        ),
        migrations.AlterField(
            model_name='formapagocompra',
            name='plazo_compra',
            field=models.PositiveIntegerField(help_text=b'En caso de Credito establecer el plazo de tiempo en dias para el pago.', verbose_name=b'Plazo de Pago Compra'),
        ),
        migrations.AlterField(
            model_name='formapagoventa',
            name='forma_pago_venta',
            field=models.CharField(max_length=2, verbose_name=b'Forma de Pago Venta', choices=[(b'CO', b'Contado'), (b'TC', b'Tarjeta de Credito'), (b'TD', b'Tarjeta de Debito')]),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='numero_mesa',
            field=models.PositiveIntegerField(help_text=b'Ingrese el Numero de Mesa.', unique=True, verbose_name=b'Numero de Mesa'),
        ),
        migrations.AlterField(
            model_name='mesaubicacion',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion de la Ubicacion de la Mesa. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Descripcion de la Ubicacion'),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='abreviacion_moneda',
            field=models.CharField(help_text=b'Abreviacion o simbolo de la Moneda. EJ: Guaranies - Gs.', unique=True, max_length=5, verbose_name=b'Abreviacion de la Moneda'),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='codigo_moneda',
            field=models.IntegerField(help_text=b'Corresponde al codigo internacional ISO 4217 de la Moneda. EJ: Gs - 600', unique=True, verbose_name=b'Codigo de Moneda ISO 4217'),
        ),
        migrations.AlterField(
            model_name='tipodeposito',
            name='tipo_deposito',
            field=models.CharField(help_text=b'Ingrese el identificador del Tipo de Deposito. (Hasta 2 caracteres)', unique=True, max_length=2, verbose_name=b'Tipo de Deposito'),
        ),
    ]
