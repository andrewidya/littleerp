# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0005_auto_20160914_1741'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='payroll',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='payroll',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='payroll',
            name='employee',
        ),
    ]
