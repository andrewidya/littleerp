# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0023_evaluation_rate'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='evaluationdetail',
            unique_together=set([('evaluation', 'eval_item')]),
        ),
    ]
