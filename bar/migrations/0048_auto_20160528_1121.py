# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0047_auto_20160524_1338'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compraestado',
            options={'verbose_name': 'Compra - Estado', 'verbose_name_plural': 'Compras - Estados'},
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 28, 15, 21, 52, 833000, tzinfo=utc), help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual.'),
        ),
    ]
