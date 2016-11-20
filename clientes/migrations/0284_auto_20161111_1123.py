# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0283_auto_20161111_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='cliente_documento_reserva',
            field=models.CharField(help_text=b'Seleccione el Documento del Cliente el cual se registrara en la Reserva.', max_length=50, verbose_name=b'Documento'),
        ),
    ]
