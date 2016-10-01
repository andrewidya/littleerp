# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0020_auto_20160928_1318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluation',
            old_name='date_created',
            new_name='date_create',
        ),
    ]
