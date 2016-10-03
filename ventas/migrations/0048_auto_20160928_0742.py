# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0047_auto_20160927_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aperturacaja',
            name='caja',
            field=models.ForeignKey(verbose_name=b'Caja', to='bar.Caja', help_text=b'Seleccione la Caja a aperturar.'),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='estado_apertura_caja',
            field=models.CharField(max_length=3, verbose_name=b'Estado', choices=[(b'VIG', b'Vigente'), (b'CER', b'Cerrada')]),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_apertura_caja',
            field=models.DateField(default=datetime.date.today, help_text=b'Fecha en la que se realiza la Apertura de Caja.', verbose_name=b'Fecha Apertura'),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_registro_apertura_caja',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha/hora registro'),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='horario',
            field=models.ForeignKey(to='personal.Horario'),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='monto_apertura',
            field=models.DecimalField(default=0, help_text=b'Ingrese el monto de efectivo utilizado para aperturar la Caja.', verbose_name=b'Monto Apertura', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='cierrecaja',
            name='apertura_caja',
            field=models.ForeignKey(verbose_name=b'Cajas Aperturadas', to='ventas.AperturaCaja', help_text=b'Seleccione la Caja a cerrar.'),
        ),
        migrations.AlterField(
            model_name='cierrecaja',
            name='fecha_hora_registro_cierre_caja',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha/hora registro'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='cliente_factura',
            field=models.ForeignKey(help_text=b'Corrobore con el Cliente si son correctos sus datos antes de confirmar la Venta.', to='clientes.Cliente'),
        ),
    ]
