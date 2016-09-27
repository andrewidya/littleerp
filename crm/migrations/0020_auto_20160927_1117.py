# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0019_auto_20160927_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satisficationdetail',
            name='value',
            field=models.PositiveIntegerField(verbose_name='Point Value'),
        ),
    ]
