# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0231_auto_20160816_1318'),
        ('personal', '0251_auto_20160816_1318'),
        ('stock', '0178_auto_20160816_0739'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransferenciaStock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_existente_stock', models.DecimalField(default=0, help_text=b'Despliega la cantidad existente del Producto.', verbose_name=b'Cantidad Existente', max_digits=10, decimal_places=3)),
                ('cantidad_producto_transferencia', models.DecimalField(help_text=b'Cantidad a Transferir del producto.', verbose_name=b'Cantidad a Transferir', max_digits=10, decimal_places=3)),
                ('fecha_hora_registro_transferencia', models.DateTimeField(help_text=b'La fecha y hora se asignan al momento de guardar los datos de la Transferencia. No se requiere el ingreso de este dato.', verbose_name=b'Fecha/hora registro transferencia', auto_now_add=True)),
                ('deposito_proveedor_transferencia', models.ForeignKey(related_name='deposito_proveedor', verbose_name=b'Deposito Proveedor', to='bar.Deposito', help_text=b'Seleccione el Deposito que se encargara de procesar la Transferencia.')),
                ('deposito_solicitante_transferencia', models.ForeignKey(related_name='deposito_solicitante', verbose_name=b'Deposito Solicitante', to='bar.Deposito', help_text=b'Seleccione el Deposito desde donde se solicita la Transferencia.')),
                ('estado_transferencia', models.ForeignKey(to='bar.TransferenciaStockEstado')),
                ('producto_transferencia', models.ForeignKey(related_name='producto_solicitado', verbose_name=b'Producto a Transferir', to='stock.Stock', help_text=b'Seleccione el producto a Transferir entre depositos.')),
                ('usuario_autorizante_transferencia', models.ForeignKey(related_name='usuario_autorizante', verbose_name=b'Usuario Autorizante', to='personal.Empleado', help_text=b'El usuario logueado que autorice la solicitud de Transferencia sera registrado automaticamente como el Autorizante.')),
                ('usuario_solicitante_transferencia', models.ForeignKey(related_name='usuario_solicitante', verbose_name=b'Usuario Solicitante', to='personal.Empleado', help_text=b'El usuario logueado que realice la solicitud de Transferencia sera registrado automaticamente como el Solicitante.')),
            ],
            options={
                'verbose_name': 'Transferencias de Productos entre Depositos',
                'verbose_name_plural': 'Transferencias de Productos entre Depositos',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='cantidad_existente_stock',
            field=models.DecimalField(default=0, help_text=b'Corresponde a la cantidad existente del Producto registrada en la tabla Stock.', verbose_name=b'Cantidad Existente', max_digits=10, decimal_places=3),
        ),
        migrations.CreateModel(
            name='ConfirmaTransferenciaStock',
            fields=[
            ],
            options={
                'verbose_name': 'Stock - Confirmacion de Transferencia de Producto entre Deposito',
                'proxy': True,
                'verbose_name_plural': 'Stock - Confirmaciones de Transferencias de Productos entre Depositos',
            },
            bases=('stock.transferenciastock',),
        ),
        migrations.CreateModel(
            name='SolicitaTransferenciaStock',
            fields=[
            ],
            options={
                'verbose_name': 'Stock - Confirmacion de Transferencia de Producto entre Deposito',
                'proxy': True,
                'verbose_name_plural': 'Stock - Confirmaciones de Transferencias de Productos entre Depositos',
            },
            bases=('stock.transferenciastock',),
        ),
    ]
