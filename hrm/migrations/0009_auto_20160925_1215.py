# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0008_auto_20160925_1212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bankname',
            old_name='bank_name',
            new_name='name',
        ),
    ]
