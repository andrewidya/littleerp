# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0027_auto_20161011_1910'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operational', '0007_auto_20161011_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('base_salary', models.DecimalField(null=True, verbose_name=b'Base Salary', max_digits=12, decimal_places=2, blank=True)),
                ('contract', models.ForeignKey(verbose_name=b'Employee \t\t\t\t\t\t\t\tcontract', to='hrm.EmployeeContract')),
                ('period', models.ForeignKey(verbose_name=b'Period', to='operational.PayrollPeriod')),
                ('staff', models.ForeignKey(verbose_name=b'User Staff', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
