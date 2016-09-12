# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0010_auto_20160911_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='period',
            field=models.ForeignKey(default='', to='hrm.EvaluationPeriod'),
            preserve_default=False,
        ),
    ]
