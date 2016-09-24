# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_auto_20160924_1434'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicesalarydetail',
            options={'verbose_name': 'Detail Salary on Service', 'verbose_name_plural': 'Detail Salary on Service'},
        ),
    ]
