# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_auto_20160912_0508'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name': 'Customer Branch Office', 'verbose_name_plural': 'Customer Branch Offices', 'permissions': (('can_view', 'Can view available branch'),)},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Customer List', 'verbose_name_plural': 'Customer Information', 'permissions': (('can_view', 'Can view available customer'),)},
        ),
    ]
