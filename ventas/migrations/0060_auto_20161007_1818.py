# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0059_ventaocasional_ventaocasionaldetalle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aperturacaja',
            name='fecha_apertura_caja',
        ),
        migrations.AddField(
            model_name='aperturacaja',
            name='fecha_hora_apertura_caja',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 7, 21, 17, 57, 150000, tzinfo=utc), help_text=b'Fecha en la que se realiza la Apertura de Caja.', verbose_name=b'Fecha Apertura'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='cliente_factura',
            field=models.ForeignKey(blank=True, to='clientes.Cliente', help_text=b'Corrobore con el Cliente si son correctos sus datos antes de confirmar la Venta.', null=True, verbose_name=b'Cliente'),
        ),
        # migrations.AlterField(
        #     model_name='venta',
        #     name='forma_pago',
        #     field=models.ForeignKey(verbose_name=b'Forma de Pago', to='bar.FormaPagoVenta', help_text=b'Seleccione la Forma de Pago.'),
        # ),
        migrations.AlterField(
            model_name='venta',
            name='numero_pedido',
            field=models.OneToOneField(null=True, to='ventas.Pedido', blank=True, help_text=b'Seleccione el Numero de Pedido para el cual se registrara la Venta.', verbose_name=b'Numero de Pedido'),
        ),
    ]
