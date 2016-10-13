# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0003_auto_20161010_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payrollperiod',
            name='period',
            field=models.CharField(max_length=15, null=True, verbose_name=b'Period', blank=True),
        ),
    ]
