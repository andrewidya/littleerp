# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20160912_0501'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Customer List', 'verbose_name_plural': 'Customer Information', 'permissions': (('can_view', 'Can view available customer'),)},
        ),
    ]
