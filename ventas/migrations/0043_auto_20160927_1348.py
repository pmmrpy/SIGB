# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0276_auto_20160827_2010'),
        ('ventas', '0042_auto_20160926_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aperturacaja',
            name='caja',
        ),
        migrations.RemoveField(
            model_name='aperturacaja',
            name='cajero',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='fecha_venta',
            new_name='fecha_hora_venta',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='caja',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='reserva',
        ),
        migrations.AddField(
            model_name='comanda',
            name='tiempo_estimado_elaboracion',
            field=models.TimeField(help_text=b'Corresponde al tiempo estimado que tomara elaborar el Producto Compuesto', verbose_name=b'Tiempo Estimado Elaboracion'),
        ),
        migrations.AddField(
            model_name='venta',
            name='cliente_factura',
            field=models.ForeignKey(default=1, to='clientes.Cliente', help_text=b'Corrobore con el Cliente si son correctos sus datos antes de confirmar la Venta.'),
        ),
        migrations.AddField(
            model_name='venta',
            name='entrega_reserva',
            field=models.DecimalField(default=0, help_text=b'Monto entregado por la Reserva. Este monto se acredita en consumision y se descuenta del Total de la Venta.', verbose_name=b'Entrega Reserva', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='venta',
            name='empresa',
            field=models.ForeignKey(default=9, to='compras.Empresa'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='numero_factura_venta',
            field=models.ForeignKey(related_name='numero_factura', default=1, verbose_name=b'Numero de Factura de la Venta', to='bar.FacturaVenta', help_text=b''),
        ),
        migrations.DeleteModel(
            name='AperturaCaja',
        ),
    ]
