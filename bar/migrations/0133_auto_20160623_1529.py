# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0132_auto_20160623_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='codigociudadoperadoratelefono',
            name='ciudad_operadora',
            field=models.ForeignKey(default=1, verbose_name=b'Descripcion Ciudad/Operadora', to='bar.Ciudad', help_text=b'Descripcion de la ciudad o de la operadora de telefonia movil.'),
        ),
        migrations.AddField(
            model_name='codigopaistelefono',
            name='pais',
            field=models.ForeignKey(default=1, to='bar.Pais', help_text=b'Pais al cual corresponde el codigo.'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 23, 19, 29, 10, 288000, tzinfo=utc), help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual.'),
        ),
    ]
