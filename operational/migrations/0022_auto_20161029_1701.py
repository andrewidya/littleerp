# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0021_finalpayrolldetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='payrollperiod',
            name='state',
            field=django_fsm.FSMField(default=b'OPEN', max_length=50, choices=[(b'DRAFT', b'DRAFT'), (b'FINAL', b'FINAL'), (b'PAID', b'PAID'), (b'OPEN', b'OPEN'), (b'CLOSE', b'CLOSE')]),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='state',
            field=django_fsm.FSMField(default=b'DRAFT', max_length=50, choices=[(b'DRAFT', b'DRAFT'), (b'FINAL', b'FINAL'), (b'PAID', b'PAID'), (b'OPEN', b'OPEN'), (b'CLOSE', b'CLOSE')]),
        ),
    ]
