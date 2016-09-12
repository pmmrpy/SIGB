# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0195_auto_20160830_1917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='precio_compra_sugerido',
            new_name='precio_compra',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='precio_venta_sugerido',
            new_name='precio_venta',
        ),
        migrations.AlterField(
            model_name='producto',
            name='contenido',
            field=models.DecimalField(help_text=b'Ingrese la cantidad del Producto contenida en el envase de acuerdo a su Unidad de Medida. Los Productos del tipo Insumos comprados a granel (no envasados) siempre deben ser registrados con contenido igual a una unidad. Ej: Queso - 1 kilo, Detergente - 1 litro.', verbose_name=b'Cantidad Contenido', max_digits=10, decimal_places=3),
        ),
    ]
