# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0107_auto_20160620_1304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='caja',
            options={'verbose_name': 'Caja', 'verbose_name_plural': 'Cajas'},
        ),
        migrations.AlterModelOptions(
            name='deposito',
            options={'verbose_name': 'Deposito', 'verbose_name_plural': 'Depositos'},
        ),
        migrations.AlterModelOptions(
            name='documento',
            options={'verbose_name': 'Documento', 'verbose_name_plural': 'Documentos'},
        ),
        migrations.AlterModelOptions(
            name='mesa',
            options={'verbose_name': 'Mesa', 'verbose_name_plural': 'Mesas'},
        ),
        migrations.AlterModelOptions(
            name='moneda',
            options={'verbose_name': 'Moneda', 'verbose_name_plural': 'Monedas'},
        ),
        migrations.AlterModelOptions(
            name='persona',
            options={'verbose_name': 'Persona', 'verbose_name_plural': 'Personas'},
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 22, 18, 14, 4, 145000, tzinfo=utc), help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual.'),
        ),
    ]
