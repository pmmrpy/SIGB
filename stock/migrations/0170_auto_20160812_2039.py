# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0169_stockdetalle_tipo_movimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transferenciastock',
            name='deposito_proveedor_transferencia',
        ),
        migrations.RemoveField(
            model_name='transferenciastock',
            name='deposito_solicitante_transferencia',
        ),
        migrations.RemoveField(
            model_name='transferenciastock',
            name='estado_transferencia',
        ),
        migrations.RemoveField(
            model_name='transferenciastock',
            name='producto_transferencia',
        ),
        migrations.RemoveField(
            model_name='transferenciastock',
            name='usuario_autorizante_transferencia',
        ),
        migrations.RemoveField(
            model_name='transferenciastock',
            name='usuario_solicitante_transferencia',
        ),
        migrations.DeleteModel(
            name='TransferenciaStock',
        ),
    ]
