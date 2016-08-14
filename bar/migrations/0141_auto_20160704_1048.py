# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0140_auto_20160628_1534'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='codigooperadoratelefono',
            options={'verbose_name': 'Telefono - Codigo por operadora', 'verbose_name_plural': 'Telefonos - Codigos por operadora'},
        ),
        migrations.AlterField(
            model_name='codigooperadoratelefono',
            name='codigo_operadora_telefono',
            field=models.IntegerField(help_text=b'Codigo de la operadora de telefonia.', verbose_name=b'Codigo Operadora'),
        ),
        migrations.AlterField(
            model_name='codigopaistelefono',
            name='pais',
            field=models.OneToOneField(to='bar.Pais', help_text=b'Pais al cual corresponde el codigo.'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 4, 14, 48, 34, 341000, tzinfo=utc), help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual.'),
        ),
    ]
