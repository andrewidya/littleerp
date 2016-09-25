# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0007_auto_20160925_0118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bankname',
            old_name='name',
            new_name='bank_name',
        ),
    ]
