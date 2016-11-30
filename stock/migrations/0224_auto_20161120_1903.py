# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0223_stockdepositoajusteinventario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ajustestockdetalle',
            name='cantidad_ajustar_producto',
            field=models.DecimalField(decimal_places=3, max_digits=10, blank=True, help_text=b'Ingrese la cantidad a ajustar del Producto. Debe ingresar la cantidad del Producto que finalmente quedara registrada en el Inventario.', null=True, verbose_name=b'Cantidad Ajuste'),
        ),
        migrations.AlterField(
            model_name='ajustestockdetalle',
            name='motivo_ajuste',
            field=models.CharField(help_text=b'Ingrese el motivo por el cual se realiza el Ajuste de Inventario del Producto seleccionado.', max_length=100, null=True, verbose_name=b'Motivo del Ajuste', blank=True),
        ),
    ]
