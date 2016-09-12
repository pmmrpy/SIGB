# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0035_auto_20160815_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='monto_entrega_reserva',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=18, blank=True, help_text=b'Ingrese el monto a pagar por la Reserva. Este monto luego se acredita en consumision.', verbose_name=b'Monto Entrega'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='reserva',
            field=models.ForeignKey(blank=True, to='clientes.Reserva', help_text=b'Seleccione una Reserva en caso de que el Cliente haya realizado una.', null=True),
        ),
    ]
