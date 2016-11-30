# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0419_auto_20161123_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategoriaproducto',
            name='subcategoria',
            field=models.CharField(help_text=b'Ingrese el identificador de la SubCategoria de los productos. (Hasta 3 caracteres)', unique=True, max_length=3, verbose_name=b'SubCategoria'),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 11, 29, 10, 30, 56, 652000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
    ]
