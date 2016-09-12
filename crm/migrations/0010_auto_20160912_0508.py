# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_auto_20160912_0507'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name': 'Customer Branch Office', 'verbose_name_plural': 'Customer Branch Offices', 'permissions': (('view_customer', 'Can view available branch'),)},
        ),
    ]
