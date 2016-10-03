# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0200_auto_20160926_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimientostock',
            name='tipo_movimiento',
            field=models.CharField(help_text=b'Seleccione el identificador del Tipo de Movimiento de Stock.', max_length=2, verbose_name=b'Tipo de Movimiento', choices=[(b'VE', b'Venta'), (b'CO', b'Compra'), (b'TR', b'Transferencias')]),
        ),
    ]
