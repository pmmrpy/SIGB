# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0181_auto_20160816_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferenciastock',
            name='estado_transferencia',
            field=models.ForeignKey(default=1, verbose_name=b'Estado Transferencia', to='bar.TransferenciaStockEstado', help_text=b'El estado de la Transferencia se asigna de forma automatica.'),
        ),
        migrations.AlterField(
            model_name='transferenciastock',
            name='fecha_hora_registro_transferencia',
            field=models.DateTimeField(help_text=b'La fecha y hora se asignan al momento de guardar los datos de la Transferencia. No se requiere el ingreso de este dato.', verbose_name=b'Fecha/hora registro Transferencia', auto_now_add=True),
        ),
    ]
