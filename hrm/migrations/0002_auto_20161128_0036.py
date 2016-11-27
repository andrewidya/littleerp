# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='ranking',
            field=models.CharField(max_length=6, verbose_name='Ranking', blank=True),
        ),
    ]
