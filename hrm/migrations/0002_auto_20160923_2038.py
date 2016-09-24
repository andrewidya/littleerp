# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Employee Information', 'verbose_name_plural': 'Employee Lists'},
        ),
        migrations.AlterModelOptions(
            name='leavetype',
            options={'verbose_name': 'Leave Type', 'verbose_name_plural': 'Leave Types'},
        ),
    ]
