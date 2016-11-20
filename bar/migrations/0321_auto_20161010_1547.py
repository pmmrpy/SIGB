# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0320_auto_20161010_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sector',
            name='deposito',
            field=models.ForeignKey(to='bar.Deposito', null=True),
        ),
        migrations.AlterField(
            model_name='sector',
            name='sector',
            field=models.CharField(help_text=b'Seleccione el identificador del Sector.', max_length=3, verbose_name=b'Sector', choices=[(b'DCE', b'Deposito Central'), (b'BPR', b'Barra Principal'), (b'BAR', b'Barra Arriba'), (b'BAI', b'Barrita'), (b'COC', b'Cocina'), (b'ADM', b'Administracion')]),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 10, 10, 15, 47, 36, 73000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
    ]
