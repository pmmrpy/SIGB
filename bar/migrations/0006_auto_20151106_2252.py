# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0005_auto_20151106_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='moneda',
            name='abreviacion_moneda',
            field=models.CharField(default=b'US$', help_text=b'Abreviacion o simbolo de la moneda. EJ: Guaranies - Gs.', max_length=5),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='codigo_moneda',
            field=models.IntegerField(help_text=b'Corresponde al codigo internacional de la moneda. EJ: Gs - 6900'),
        ),
    ]
