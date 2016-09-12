# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0183_auto_20160816_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferenciastock',
            name='usuario_autorizante_transferencia',
            field=models.ForeignKey(related_name='usuario_autorizante', to_field=b'usuario', blank=True, to='personal.Empleado', help_text=b'El usuario logueado que autorice la solicitud de Transferencia sera registrado automaticamente como el Autorizante.', null=True, verbose_name=b'Usuario Autorizante'),
        ),
    ]
