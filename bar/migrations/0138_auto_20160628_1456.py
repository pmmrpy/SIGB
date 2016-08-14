# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0137_auto_20160628_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodigoOperadoraTelefono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_operadora_telefono', models.IntegerField(default=21, help_text=b'Codigo de ciudad o de la operadora de telefonia movil.', verbose_name=b'Codigo Ciudad/Operadora')),
                ('tipo_operadora', models.CharField(default=b'TM', help_text=b'Tipo de Telefonia', max_length=2, choices=[(b'TM', b'Telefonia Movil'), (b'TF', b'Telefonia Fija')])),
            ],
            options={
                'verbose_name': 'Telefono - Codigo por ciudad/operadora',
                'verbose_name_plural': 'Telefonos - Codigos por ciudad/operadora',
            },
        ),
        migrations.AlterUniqueTogether(
            name='codigociudadoperadoratelefono',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='codigociudadoperadoratelefono',
            name='ciudad_operadora',
        ),
        migrations.RemoveField(
            model_name='codigociudadoperadoratelefono',
            name='codigo_pais_telefono',
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 28, 18, 56, 19, 305000, tzinfo=utc), help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual.'),
        ),
    ]
