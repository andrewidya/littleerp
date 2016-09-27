# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0012_auto_20160927_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='bank',
            field=models.ForeignKey(verbose_name='Bank', blank=True, to='hrm.BankName', null=True),
        ),
    ]
