# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0003_auto_20160914_1736'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='payrolldecreasedetail',
            unique_together=set([('employee', 'customer', 'item')]),
        ),
        migrations.AlterUniqueTogether(
            name='payrollincreasedetail',
            unique_together=set([('employee', 'customer', 'item')]),
        ),
    ]
