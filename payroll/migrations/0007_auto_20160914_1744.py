# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0006_auto_20160914_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payrolldecreasedetail',
            name='payroll',
            field=models.ForeignKey(to='payroll.Payroll'),
        ),
        migrations.AlterField(
            model_name='payrollincreasedetail',
            name='payroll',
            field=models.ForeignKey(to='payroll.Payroll'),
        ),
    ]
