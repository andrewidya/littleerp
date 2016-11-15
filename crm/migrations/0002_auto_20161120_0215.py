# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='satisficationdetail',
            options={'verbose_name': 'Satisfication Detail', 'verbose_name_plural': 'Satisfication Details'},
        ),
        migrations.AlterModelOptions(
            name='satisficationpointcategory',
            options={'verbose_name': 'Satisfication Category', 'verbose_name_plural': 'Satisfication Categories'},
        ),
        migrations.AlterModelOptions(
            name='satisficationpointrateitem',
            options={'verbose_name': 'Satisfication Item', 'verbose_name_plural': 'Satisfication Item'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Service Provided'},
        ),
        migrations.AlterModelOptions(
            name='servicesalarydetail',
            options={'verbose_name': 'Order Detail Salary', 'verbose_name_plural': 'Order Detail Salaries'},
        ),
        migrations.AlterModelOptions(
            name='servicesalaryitem',
            options={'verbose_name': 'Pricing Item', 'verbose_name_plural': 'Pricing Items'},
        ),
    ]
