# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0010_auto_20160925_2022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Employee Information', 'verbose_name_plural': 'Employee Lists', 'permissions': (('hrm_employee_view', 'Can view only'),)},
        ),
    ]
