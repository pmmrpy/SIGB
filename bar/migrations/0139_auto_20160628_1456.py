# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0138_auto_20160628_1456'),
        ('clientes', '0163_auto_20160628_1456'),
        ('compras', '0056_auto_20160628_1456'),
        ('personal', '0159_auto_20160628_1456'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CodigoCiudadOperadoraTelefono',
        ),
        migrations.AddField(
            model_name='codigooperadoratelefono',
            name='codigo_pais_telefono',
            field=models.ForeignKey(to='bar.CodigoPaisTelefono'),
        ),
        migrations.AlterUniqueTogether(
            name='codigooperadoratelefono',
            unique_together=set([('codigo_pais_telefono', 'codigo_operadora_telefono')]),
        ),
    ]
