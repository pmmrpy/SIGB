# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0182_auto_20160816_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferenciastock',
            name='usuario_autorizante_transferencia',
            field=models.ForeignKey(related_name='usuario_autorizante', verbose_name=b'Usuario Autorizante', to_field=b'usuario', to='personal.Empleado', help_text=b'El usuario logueado que autorice la solicitud de Transferencia sera registrado automaticamente como el Autorizante.'),
        ),
        migrations.AlterField(
            model_name='transferenciastock',
            name='usuario_solicitante_transferencia',
            field=models.ForeignKey(related_name='usuario_solicitante', verbose_name=b'Usuario Solicitante', to_field=b'usuario', to='personal.Empleado', help_text=b'El usuario logueado que realice la solicitud de Transferencia sera registrado automaticamente como el Solicitante.'),
        ),
    ]
