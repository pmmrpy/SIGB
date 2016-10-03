# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0053_comanda_venta_ventadetalle'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidodetalle',
            name='anulado',
            field=models.BooleanField(default=False, help_text=b'Seleccione esta casilla si desea anular el Producto solicitado.', verbose_name=b'Anular?'),
        ),
        migrations.AddField(
            model_name='pedidodetalle',
            name='procesado',
            field=models.BooleanField(default=False, help_text=b'Esta casilla se marca cuando el Pedido es procesado por el Deposito correspondiente.', verbose_name=b'Procesado?'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha_pedido',
            field=models.DateTimeField(help_text=b'La fecha y hora del Pedido se asignaran automaticamente una vez que sea guardado.', verbose_name=b'Fecha/Hora del Pedido', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='mesa_pedido',
            field=models.ManyToManyField(help_text=b'Indique la/s mesa/s que sera/n ocupada/s por el/los Cliente/s.', to='bar.Mesa', verbose_name=b'Mesas'),
        ),
    ]
