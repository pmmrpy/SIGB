# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0290_auto_20160927_1409'),
        ('personal', '0272_auto_20160827_2010'),
        ('ventas', '0043_auto_20160927_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='AperturaCaja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto_apertura', models.DecimalField(default=0, help_text=b'Ingrese el monto de efectivo utilizado para aperturar la Caja.', verbose_name=b'Monto usado en Apertura', max_digits=18, decimal_places=0)),
                ('fecha_apertura_caja', models.DateField(auto_now_add=True)),
                ('fecha_hora_registro_apertura_caja', models.DateTimeField(auto_now_add=True)),
                ('estado_apertura_caja', models.CharField(max_length=3, choices=[(b'VIG', b'Vigente'), (b'CER', b'Cerrada')])),
                ('caja', models.ForeignKey(verbose_name=b'Caja a Aperturar', to='bar.Caja', help_text=b'Seleccione la Caja a aperturar.')),
                ('cajero', models.ForeignKey(verbose_name=b'Cajero', to='personal.Empleado', help_text=b'Seleccione el Cajero que realizara movimientos en esta Caja.')),
                ('horario', models.ForeignKey(to='personal.Horario')),
            ],
            options={
                'verbose_name': 'Apertura de Caja',
                'verbose_name_plural': 'Cajas - Aperturas',
            },
        ),
        migrations.CreateModel(
            name='CierreCaja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_hora_registro_cierre_caja', models.DateTimeField(auto_now_add=True)),
                ('monto_registro_efectivo', models.DecimalField(default=0, help_text=b'', verbose_name=b'Monto Registrado Efectivo', max_digits=18, decimal_places=0)),
                ('rendicion_efectivo', models.DecimalField(default=0, help_text=b'', verbose_name=b'Monto Rendicion Efectivo', max_digits=18, decimal_places=0)),
                ('diferencia_efectivo', models.DecimalField(default=0, help_text=b'', verbose_name=b'Diferencia Registro/Rendicion Efectivo', max_digits=18, decimal_places=0)),
                ('monto_registro_tcs', models.DecimalField(default=0, help_text=b'', verbose_name=b'Monto Registrado TCs', max_digits=18, decimal_places=0)),
                ('rendicion_tcs', models.DecimalField(default=0, help_text=b'', verbose_name=b'Monto Rendicion TCs', max_digits=18, decimal_places=0)),
                ('diferencia_tcs', models.DecimalField(default=0, help_text=b'', verbose_name=b'Diferencia Registro/Rendicion TCs', max_digits=18, decimal_places=0)),
                ('monto_registro_tds', models.DecimalField(default=0, help_text=b'', verbose_name=b'Monto Registrado TDs', max_digits=18, decimal_places=0)),
                ('rendicion_tds', models.DecimalField(default=0, help_text=b'', verbose_name=b'Monto Rendicion TDs', max_digits=18, decimal_places=0)),
                ('diferencia_tds', models.DecimalField(default=0, help_text=b'', verbose_name=b'Diferencia Registro/Rendicion TDs', max_digits=18, decimal_places=0)),
                ('monto_registro_otros_medios', models.DecimalField(default=0, help_text=b'', verbose_name=b'Monto Registrado Otros Medios', max_digits=18, decimal_places=0)),
                ('rendicion_otros_medios', models.DecimalField(default=0, help_text=b'', verbose_name=b'Monto Rendicion Otros Medios', max_digits=18, decimal_places=0)),
                ('diferencia_otros_medios', models.DecimalField(default=0, help_text=b'', verbose_name=b'Diferencia Registro/Rendicion Otros Medios', max_digits=18, decimal_places=0)),
                ('apertura_caja', models.ForeignKey(to='ventas.AperturaCaja')),
            ],
            options={
                'verbose_name': 'Cierre de Caja',
                'verbose_name_plural': 'Cajas - Cierres',
            },
        ),
    ]
