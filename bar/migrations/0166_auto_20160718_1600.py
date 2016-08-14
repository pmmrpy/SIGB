# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0165_auto_20160715_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 18, 20, 0, 40, 831000, tzinfo=utc), help_text=b'Registra la fecha y hora en la que se definio la Cotizacion. Corresponde a la fecha y hora actual.', verbose_name=b'Fecha de Cotizacion'),
        ),
        migrations.AlterField(
            model_name='subcategoriaproducto',
            name='subcategoria',
            field=models.CharField(help_text=b'Ingrese el identificador de la SubCategoria de los productos. (Hasta 3 caracteres)', max_length=3, verbose_name=b'SubCategoria'),
        ),
    ]
