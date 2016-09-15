# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0014_auto_20160912_1115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='divison',
            new_name='division',
        ),
    ]
