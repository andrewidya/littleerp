# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0024_auto_20160930_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluation',
            name='rate',
        ),
        migrations.AddField(
            model_name='evaluation',
            name='ranking',
            field=models.CharField(default='--', max_length=6, verbose_name='Ranking'),
            preserve_default=False,
        ),
    ]
