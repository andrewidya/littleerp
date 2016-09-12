# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0011_evaluation_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluationitem',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
