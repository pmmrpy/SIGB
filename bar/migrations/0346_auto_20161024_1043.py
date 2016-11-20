# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0345_auto_20161024_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facturaventa',
            name='empresa',
        ),
        migrations.AddField(
            model_name='facturaventa',
            name='timbrado',
            field=models.ForeignKey(default=2, to='bar.Timbrado'),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 10, 24, 10, 43, 38, 557000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
    ]
