# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0322_auto_20161010_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja',
            name='sector',
            field=models.ForeignKey(to='bar.Sector'),
        ),
        migrations.AlterField(
            model_name='categoriaproducto',
            name='categoria',
            field=models.CharField(help_text=b'Ingrese el identificador de la Categoria de los productos. (Hasta 2 caracteres)', unique=True, max_length=2, verbose_name=b'Categoria', choices=[(b'BE', b'Bebidas'), (b'CO', b'Comidas'), (b'CI', b'Cigarrillos'), (b'GO', b'Golosinas'), (b'AL', b'Articulos de Limpieza')]),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 10, 13, 19, 59, 26, 68000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
    ]
