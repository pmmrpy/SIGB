# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0187_auto_20160823_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='unidad_medida_contenido',
        ),
        migrations.AddField(
            model_name='producto',
            name='fecha_elaboracion',
            field=models.DateField(default=datetime.date(2016, 8, 26), help_text=b'Ingrese la fecha de elaboracion del Producto.', verbose_name=b'Fecha de Elaboracion'),
        ),
        migrations.AddField(
            model_name='producto',
            name='fecha_vencimiento',
            field=models.DateField(default=datetime.date(2016, 9, 25), help_text=b'Ingrese la fecha de vencimiento del Producto.', verbose_name=b'Fecha de Vencimiento'),
        ),
        migrations.AddField(
            model_name='producto',
            name='perecedero',
            field=models.BooleanField(default=False, help_text=b'Marque la casilla si el Producto a registrar es Perecedero.', verbose_name=b'Es perecedero?'),
        ),
        migrations.AlterField(
            model_name='transferenciastock',
            name='cantidad_existente_stock',
            field=models.DecimalField(default=0, help_text=b'Despliega la cantidad existente del Producto en el Deposito Proveedor seleccionado.', verbose_name=b'Cantidad Existente', max_digits=10, decimal_places=3),
        ),
    ]
