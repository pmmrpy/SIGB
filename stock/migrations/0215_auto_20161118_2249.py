# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0214_auto_20161118_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transferenciastock',
            name='cantidad_existente_stock',
        ),
        migrations.AlterField(
            model_name='productocompuestodetalle',
            name='cantidad_insumo',
            field=models.DecimalField(help_text=b'Ingrese la cantidad del Insumo.', verbose_name=b'Cantidad Insumo', max_digits=10, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='productocompuestodetalle',
            name='costo_promedio_insumo',
            field=models.DecimalField(help_text=b'Corresponde al costo promedio de 1 unidad del Insumo de acuerdo a su Unidad de Medida.', verbose_name=b'Costo Promedio Insumo por Un. Med.', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='transferenciastock',
            name='fecha_hora_registro_transferencia',
            field=models.DateTimeField(help_text=b'La fecha y hora de registro de la Solicitud de Transferencia se asignan al momento de guardar los datos de la misma. No se requiere el ingreso de este dato.', verbose_name=b'Fecha/hora registro solicitud Transferencia', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transferenciastock',
            name='producto_transferencia',
            field=models.ForeignKey(related_name='producto_solicitado', verbose_name=b'Producto a transferir', to='stock.Producto', help_text=b'Seleccione el producto a Transferir entre depositos.'),
        ),
    ]
