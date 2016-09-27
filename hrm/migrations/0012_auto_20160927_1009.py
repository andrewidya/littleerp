# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0011_auto_20160925_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluationdetail',
            name='eval_value',
            field=models.PositiveIntegerField(verbose_name='Value'),
        ),
    ]
