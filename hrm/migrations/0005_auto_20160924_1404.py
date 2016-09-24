# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_auto_20160921_0848'),
        ('hrm', '0004_auto_20160923_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeContract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('contract_status', models.CharField(max_length=8, blank=True)),
                ('basic_salary', models.DecimalField(null=True, verbose_name='Basic Salary', max_digits=12, decimal_places=2, blank=True)),
                ('calculate_condition', models.CharField(help_text='Condition needed for calculate total salary', max_length=1, verbose_name='Calculating Condition', choices=[(b'+', b'Adding Total Salary'), (b'-', b'Decreasing Total Salary')])),
                ('reference', models.CharField(max_length=255, blank=True)),
                ('employee', models.ForeignKey(verbose_name='Employee', to='hrm.Employee')),
                ('service_related', models.ForeignKey(related_name='service_order', verbose_name='Customer Demand Relating', to='crm.SalesOrderDetail', help_text='This info related to the service needed by customer as detail of sales order')),
            ],
            options={
                'verbose_name': 'Employee Contract',
                'verbose_name_plural': 'Employee Contracts',
            },
        ),
        migrations.CreateModel(
            name='OtherSalary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.DecimalField(verbose_name='Value', max_digits=12, decimal_places=2)),
                ('employee_contract', models.ForeignKey(related_name='employee_contract', verbose_name='Employee Contract', to='hrm.EmployeeContract')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Salary Category')),
            ],
            options={
                'verbose_name': 'Salary Category',
                'verbose_name_plural': 'Salary Categories',
            },
        ),
        migrations.CreateModel(
            name='SalaryName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Salary Name')),
                ('salary_category', models.ForeignKey(related_name='salary_category', to='hrm.SalaryCategory')),
            ],
            options={
                'verbose_name': 'Salary Name',
                'verbose_name_plural': 'Salaries Name',
            },
        ),
        migrations.AddField(
            model_name='othersalary',
            name='salary_name',
            field=models.ForeignKey(related_name='salary_name', verbose_name='Salary Name', to='hrm.SalaryName'),
        ),
    ]
