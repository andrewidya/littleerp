# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0017_auto_20161016_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='state',
            field=django_fsm.FSMField(default=b'draft', max_length=50),
        ),
    ]
