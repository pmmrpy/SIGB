# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0144_auto_20160704_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategoriaproducto',
            name='categoria',
            field=models.ForeignKey(default=3, to='bar.CategoriaProducto'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 4, 17, 52, 44, 349000, tzinfo=utc), help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual.'),
        ),
    ]
