# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0187_auto_20160807_2113'),
        ('ventas', '0026_auto_20160804_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aperturacaja',
            name='caja',
            field=models.ForeignKey(verbose_name=b'', to='bar.Caja', help_text=b''),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='cajero',
            field=models.ForeignKey(verbose_name=b'', to='personal.Empleado', help_text=b''),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_apertura_caja',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='monto_apertura',
            field=models.DecimalField(default=0, help_text=b'Ingrese el monto de efectivo utilizado para aperturar la Caja.', verbose_name=b'Monto usado en Apertura', max_digits=18, decimal_places=0),
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='mesa_pedido',
        ),
        migrations.AddField(
            model_name='pedido',
            name='mesa_pedido',
            field=models.ManyToManyField(help_text=b'Indique la/s mesa/s que sera/n ocupada/s por el/los Cliente/s.', to='bar.Mesa', verbose_name=b'Mesas'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='total_pedido',
            field=models.DecimalField(default=0, verbose_name=b'Total del Pedido', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='pedidodetalle',
            name='total_producto_pedido',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente tomando el Precio Venta del Producto por la Cantidad del Producto.', verbose_name=b'Costo Total del Producto', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='venta',
            name='total_venta',
            field=models.DecimalField(default=0, verbose_name=b'Total de la Venta', max_digits=18, decimal_places=0),
        ),
    ]
