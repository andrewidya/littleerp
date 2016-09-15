# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0015_auto_20160912_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='account_number',
        ),
        migrations.RemoveField(
            model_name='leaverecord',
            name='branch',
        ),
        migrations.AddField(
            model_name='employee',
            name='bank_account',
            field=models.CharField(max_length=20, null=True, verbose_name='Bank Account', blank=True),
        ),
    ]
