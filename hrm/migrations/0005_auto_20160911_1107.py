# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0004_auto_20160911_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='account_number',
            field=models.CharField(max_length=20, null=True, verbose_name='Account Number', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(max_length=15, null=True, verbose_name='Phone Number', blank=True),
        ),
    ]
