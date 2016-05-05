# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0007_auto_20151106_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodigoCiudadOperadoraTelefono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_ciudad_operadora_telefono', models.IntegerField(default=21, help_text=b'Codigo de ciudad o de la operadora de telefonia movil.')),
                ('ciudad_operadora', models.CharField(help_text=b'Descripcion de la ciudad o de la operadora de telefonia movil.', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CodigoPaisTelefono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_pais_telefono', models.IntegerField(default=595, help_text=b'Codigo internacional del pais al cual corresponde el telefono.')),
                ('pais', models.CharField(help_text=b'Pais al cual corresponde el codigo.', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 14, 21, 28, 859000, tzinfo=utc), help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual'),
        ),
        migrations.AddField(
            model_name='codigociudadoperadoratelefono',
            name='codigo_pais_telefono',
            field=models.ForeignKey(to='bar.CodigoPaisTelefono'),
        ),
    ]
