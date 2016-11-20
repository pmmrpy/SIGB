# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0210_auto_20161116_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='insumo',
            field=models.ForeignKey(blank=True, to='stock.Insumo', null=True),
        ),
    ]
