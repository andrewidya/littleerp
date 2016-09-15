# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0014_auto_20160914_1648'),
        ('hrm', '0018_auto_20160914_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer', models.OneToOneField(verbose_name='Customer', to='crm.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='PayrollDecreaseDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.DecimalField(max_digits=15, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='PayrollDecreaseItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, verbose_name='Decreasing Component')),
            ],
        ),
        migrations.CreateModel(
            name='PayrollIncreaseDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.DecimalField(max_digits=15, decimal_places=2)),
                ('customer', models.ForeignKey(to='crm.Customer')),
                ('employee', models.ForeignKey(to='hrm.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='PayrollIncreaseItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, verbose_name='Increasing Component')),
            ],
        ),
        migrations.CreateModel(
            name='PayrollPeriod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='payrollincreasedetail',
            name='item',
            field=models.ForeignKey(to='payroll.PayrollIncreaseItem'),
        ),
        migrations.AddField(
            model_name='payrollincreasedetail',
            name='payroll',
            field=models.OneToOneField(to='payroll.Payroll'),
        ),
        migrations.AddField(
            model_name='payrolldecreasedetail',
            name='item',
            field=models.ForeignKey(to='payroll.PayrollDecreaseItem'),
        ),
        migrations.AddField(
            model_name='payrolldecreasedetail',
            name='payroll',
            field=models.OneToOneField(to='payroll.Payroll'),
        ),
        migrations.AddField(
            model_name='payroll',
            name='decreasing_item',
            field=models.ManyToManyField(to='payroll.PayrollDecreaseItem', through='payroll.PayrollDecreaseDetail'),
        ),
        migrations.AddField(
            model_name='payroll',
            name='employee',
            field=models.OneToOneField(verbose_name='Employee Name', to='hrm.Employee'),
        ),
        migrations.AddField(
            model_name='payroll',
            name='increasing_item',
            field=models.ManyToManyField(to='payroll.PayrollIncreaseItem', through='payroll.PayrollIncreaseDetail'),
        ),
        migrations.AddField(
            model_name='payroll',
            name='period',
            field=models.OneToOneField(verbose_name='Payrolling Period', to='payroll.PayrollPeriod'),
        ),
        migrations.AlterUniqueTogether(
            name='payrollincreasedetail',
            unique_together=set([('employee', 'customer')]),
        ),
        migrations.AlterUniqueTogether(
            name='payroll',
            unique_together=set([('customer', 'employee', 'period')]),
        ),
    ]
