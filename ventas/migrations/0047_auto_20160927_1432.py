# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0046_venta_posee_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='forma_pago',
            field=models.CharField(help_text=b'Seleccione la Forma de Pago.', max_length=2, verbose_name=b'Forma de Pago', choices=[(b'CO', b'Contado'), (b'TC', b'Tarjeta de Credito'), (b'TD', b'Tarjeta de Debito'), (b'OM', b'Otros medios')]),
        ),
    ]
