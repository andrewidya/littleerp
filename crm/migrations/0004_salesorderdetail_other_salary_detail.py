# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20160920_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorderdetail',
            name='other_salary_detail',
            field=models.ManyToManyField(related_name='other_salary_detail', through='crm.ServiceSalaryDetail', to='crm.ServiceSalaryItem'),
        ),
    ]
