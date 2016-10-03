# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0201_auto_20160926_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transferenciastock',
            old_name='deposito_solicitante_transferencia',
            new_name='deposito_destino_transferencia',
        ),
        migrations.RenameField(
            model_name='transferenciastock',
            old_name='deposito_proveedor_transferencia',
            new_name='deposito_origen_transferencia',
        ),
        migrations.AddField(
            model_name='transferenciastock',
            name='fecha_hora_autorizacion_transferencia',
            field=models.DateTimeField(auto_now=True, help_text=b'La fecha y hora se asignan al momento de autorizarse la Transferencia. No se requiere el ingreso de este dato.', null=True, verbose_name=b'Fecha/hora autorizacion Transferencia'),
        ),
        migrations.AlterField(
            model_name='movimientostock',
            name='producto_stock',
            field=models.ForeignKey(related_name='producto_stock', verbose_name=b'Producto', to='stock.Producto', help_text=b'Seleccione el Producto a registrar en el Stock.'),
        ),
    ]
