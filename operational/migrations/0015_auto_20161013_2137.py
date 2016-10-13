# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0014_auto_20161013_2133'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='payroll',
            unique_together=set([('contract', 'period')]),
        ),
    ]
