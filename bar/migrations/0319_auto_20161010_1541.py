# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0318_auto_20161010_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='sector',
            name='deposito',
            field=models.ForeignKey(default=1, to='bar.Deposito'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Sector. (Hasta 100 caracteres)', max_length=300, verbose_name=b'Descripcion del Sector'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='sector',
            field=models.CharField(help_text=b'Seleccione el identificador del Sector.', max_length=3, verbose_name=b'Sector', choices=[(b'DCE', b'Deposito Central'), (b'BPR', b'Barra Principal'), (b'BAR', b'Barra Arriba'), (b'BAI', b'Barrita'), (b'COC', b'Cocina')]),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 10, 10, 15, 41, 33, 738000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
    ]
