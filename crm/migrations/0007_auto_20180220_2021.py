# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_auto_20180220_1819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicesalarydetail',
            old_name='service_order_detail',
            new_name='sales_order_detail',
        ),
        migrations.AlterUniqueTogether(
            name='servicesalarydetail',
            unique_together=set([('sales_order_detail', 'service_salary_item')]),
        ),
    ]
