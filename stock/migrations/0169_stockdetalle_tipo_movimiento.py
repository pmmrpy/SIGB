# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0193_auto_20160809_1031'),
        ('stock', '0168_remove_stockdetalle_tipo_movimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockdetalle',
            name='tipo_movimiento',
            field=models.ForeignKey(default=1, verbose_name=b'Tipo de Movimiento', to='bar.TipoMovimientoStock', help_text=b'Seleccione el identificador del Tipo de Movimiento de Stock.'),
        ),
    ]
