# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0011_auto_20161011_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='overtime',
            field=models.DecimalField(null=True, verbose_name=b'Overtime', max_digits=12, decimal_places=2, blank=True),
        ),
    ]
