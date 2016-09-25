# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_auto_20160924_1438'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemcategory',
            options={'verbose_name': 'Salary Category', 'verbose_name_plural': 'Salary Categories'},
        ),
        migrations.AlterModelOptions(
            name='salesorderdetail',
            options={'verbose_name': 'Order Detail', 'verbose_name_plural': 'Order Details'},
        ),
        migrations.AlterModelOptions(
            name='servicesalarydetail',
            options={'verbose_name': 'Detail Salary Per Service', 'verbose_name_plural': 'Detail Salary Per Service'},
        ),
        migrations.AlterModelOptions(
            name='servicesalaryitem',
            options={'verbose_name': 'Service Salary', 'verbose_name_plural': 'Service Salaries'},
        ),
    ]
