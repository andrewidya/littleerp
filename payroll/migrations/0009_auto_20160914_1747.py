# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0008_auto_20160914_1746'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='payroll',
            unique_together=set([('employee', 'customer', 'period')]),
        ),
    ]
