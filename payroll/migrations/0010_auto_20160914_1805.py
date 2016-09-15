# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0009_auto_20160914_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payrollincreasedetail',
            name='item',
            field=models.ForeignKey(related_name='payroll_items', to='payroll.PayrollIncreaseItem'),
        ),
    ]
