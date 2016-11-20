# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0322_auto_20161010_1636'),
        ('ventas', '0065_auto_20161010_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='comanda',
            name='area_encargada',
            field=models.ForeignKey(default=2, verbose_name=b'Area Encargada', to='bar.Sector'),
        ),
    ]
