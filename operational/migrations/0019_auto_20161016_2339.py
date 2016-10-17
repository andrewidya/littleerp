# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0018_auto_20161016_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostProcessedPayroll',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('operational.payroll',),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='state',
            field=django_fsm.FSMField(default=b'DRAFT', max_length=50, choices=[(b'DRAFT', b'DRAFT'), (b'FINAL', b'FINAL'), (b'PAID', b'PAID')]),
        ),
    ]
