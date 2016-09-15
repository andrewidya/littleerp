# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20160912_0556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='branch',
        ),
    ]
