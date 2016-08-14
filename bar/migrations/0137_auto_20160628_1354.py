# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0136_auto_20160626_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codigociudadoperadoratelefono',
            name='ciudad_operadora',
            field=models.OneToOneField(default=1, to='bar.Ciudad', help_text=b'Descripcion de la ciudad o de la operadora de telefonia movil.', verbose_name=b'Descripcion Ciudad/Operadora'),
        ),
        migrations.AlterField(
            model_name='codigopaistelefono',
            name='codigo_pais_telefono',
            field=models.IntegerField(help_text=b'Codigo internacional del pais al cual corresponde el telefono.', unique=True, verbose_name=b'Codigo Pais'),
        ),
        migrations.AlterField(
            model_name='codigopaistelefono',
            name='pais',
            field=models.OneToOneField(default=1, to='bar.Pais', help_text=b'Pais al cual corresponde el codigo.'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 28, 17, 54, 4, 306000, tzinfo=utc), help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual.'),
        ),
        migrations.AlterField(
            model_name='pais',
            name='pais',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='ciudad',
            unique_together=set([('pais', 'ciudad')]),
        ),
        migrations.AlterUniqueTogether(
            name='codigociudadoperadoratelefono',
            unique_together=set([('codigo_pais_telefono', 'codigo_ciudad_operadora_telefono')]),
        ),
    ]
