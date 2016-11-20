# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0321_auto_20161010_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='caja',
            name='sector',
            field=models.ForeignKey(default=2, to='bar.Sector'),
        ),
        migrations.AddField(
            model_name='sector',
            name='operativo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sector',
            name='deposito',
            field=models.ForeignKey(blank=True, to='bar.Deposito', null=True),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 10, 10, 16, 36, 7, 446000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
    ]
