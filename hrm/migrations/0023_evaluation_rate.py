# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0022_auto_20160928_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='rate',
            field=models.CharField(default='', max_length=6, verbose_name='Rate'),
            preserve_default=False,
        ),
    ]
