# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0015_auto_20160927_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='reg_number',
            field=models.CharField(unique=True, max_length=15, verbose_name='Registration Number'),
        ),
    ]
