# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0273_empleado_sector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='sector',
            field=models.ForeignKey(help_text=b'Seleccione el sector en donde desempenara sus funciones el Empleado.', to='bar.Sector'),
        ),
    ]
