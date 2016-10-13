# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0027_auto_20161011_1910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeecontract',
            old_name='basic_salary',
            new_name='base_salary',
        ),
    ]
