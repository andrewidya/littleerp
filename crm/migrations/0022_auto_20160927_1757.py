# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0021_auto_20160927_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satisficationdetail',
            name='value',
            field=models.PositiveIntegerField(help_text='Value must be betwen 2 to 5', verbose_name='Point Value'),
        ),
    ]
