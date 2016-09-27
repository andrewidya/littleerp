# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0020_auto_20160927_1117'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='satisficationdetail',
            unique_together=set([('satisfication', 'point_rate_item')]),
        ),
    ]
