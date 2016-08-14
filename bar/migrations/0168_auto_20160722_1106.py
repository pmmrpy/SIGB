# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0167_auto_20160722_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 22, 15, 6, 31, 712000, tzinfo=utc), help_text=b'Registra la fecha y hora en la que se definio la Cotizacion. Corresponde a la fecha y hora actual.', verbose_name=b'Fecha de Cotizacion'),
        ),
        migrations.AlterField(
            model_name='unidadmedidaproducto',
            name='unidad_medida_producto',
            field=models.CharField(max_length=2, choices=[(b'UN', b'Unidad'), (b'LI', b'Litros'), (b'KG', b'Kilogramos')]),
        ),
    ]