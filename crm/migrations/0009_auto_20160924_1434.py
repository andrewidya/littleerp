# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_auto_20160924_1421'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='servicesalarydetail',
            unique_together=set([('service_order_detail', 'service_salary_item')]),
        ),
    ]
