# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quali',
            field=models.CharField(default=b'sem', max_length=3),
        ),
    ]
