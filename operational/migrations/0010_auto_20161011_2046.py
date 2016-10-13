# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0009_auto_20161011_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='staff',
            field=models.ForeignKey(verbose_name=b'User Staff', to=settings.AUTH_USER_MODEL),
        ),
    ]
