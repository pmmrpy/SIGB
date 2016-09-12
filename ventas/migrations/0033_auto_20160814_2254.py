# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0032_comanda'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aperturacaja',
            options={'verbose_name': 'Caja - Apertura', 'verbose_name_plural': 'Cajas - Aperturas'},
        ),
        migrations.AlterModelOptions(
            name='cierrecaja',
            options={'verbose_name': 'Caja - Cierre', 'verbose_name_plural': 'Cajas - Cierres'},
        ),
        migrations.AlterModelOptions(
            name='ingresovalorcaja',
            options={'verbose_name': 'Caja - Ingreso de Valores', 'verbose_name_plural': 'Cajas - Ingreso de Valores'},
        ),
        migrations.AlterModelOptions(
            name='movimientocaja',
            options={'verbose_name': 'Caja - Movimiento', 'verbose_name_plural': 'Cajas - Movimientos'},
        ),
        migrations.AlterModelOptions(
            name='retirovalorcaja',
            options={'verbose_name': 'Caja - Retiro de Valores', 'verbose_name_plural': 'Cajas - Retiro de Valores'},
        ),
    ]
