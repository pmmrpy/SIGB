# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0180_auto_20160816_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferenciastock',
            name='estado_transferencia',
            field=models.ForeignKey(default=1, to='bar.TransferenciaStockEstado'),
        ),
    ]
