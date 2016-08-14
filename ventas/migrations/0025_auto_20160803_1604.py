# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0024_auto_20160731_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='monto_entrega_reserva',
            field=models.DecimalField(default=0, help_text=b'Ingrese el monto a pagar por la Reserva. Este monto luego se acredita en consumision.', verbose_name=b'Monto Entrega', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado_pedido',
            field=models.ForeignKey(default=1, verbose_name=b'Estado del Pedido', to='bar.PedidoEstado', help_text=b'El estado del Pedido se establece automaticamente de acuerdo a...'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='mesa_pedido',
            field=models.ForeignKey(verbose_name=b'Mesas', to='bar.Mesa', help_text=b'Indique la/s mesa/s que sera/n ocupada/s por el/los Cliente/s.'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='mozo_pedido',
            field=models.ForeignKey(verbose_name=b'Atendido por?', to='personal.Empleado', help_text=b'Seleccione el personal que atendio al Cliente.'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='reserva',
            field=models.ForeignKey(help_text=b'Seleccione una Reserva en caso de que el Cliente haya realizado una.', to='clientes.Reserva'),
        ),
    ]
