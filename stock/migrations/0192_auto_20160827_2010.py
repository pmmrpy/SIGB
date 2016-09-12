# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0252_auto_20160827_2010'),
        ('stock', '0191_auto_20160827_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio_compra_sugerido',
            field=models.DecimalField(default=0, help_text=b'Precio de Compra sugerido.', verbose_name=b'Precio Compra Sugerido', max_digits=18, decimal_places=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='unidad_medida_contenido',
            field=models.ForeignKey(related_name='un_med_contenido', default=1, verbose_name=b'Unidad de Medida Presentacion', to='bar.UnidadMedidaProducto'),
        ),
    ]
