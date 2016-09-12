# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20160912_0447'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Customer List', 'verbose_name_plural': 'Customer Information', 'permissions': (('view_customer', 'Can view available customer'),)},
        ),
    ]
