# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0226_auto_20161123_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='contenido',
            field=models.DecimalField(help_text=b'Ingrese la cantidad del Producto contenida en el envase de acuerdo a su Unidad de Medida. Los Productos del tipo Insumo comprados a granel (no envasados) siempre deben ser registrados con contenido igual a una unidad. Ej: Queso - 1 kilo, Detergente - 1 litro.', verbose_name=b'Cant. Contenido', max_digits=10, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tiempo_elaboracion',
            field=models.TimeField(help_text=b'Corresponde al tiempo estimado que tomara elaborar el Producto Compuesto', null=True, verbose_name=b'Tiempo Elab.', blank=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='unidad_medida_contenido',
            field=models.ForeignKey(related_name='un_med_contenido', verbose_name=b'Un. de Med. Cont.', to='bar.UnidadMedidaProducto', help_text=b'Seleccione la Unidad de Medida del Producto contenido en su presentacion (envase).'),
        ),
    ]
