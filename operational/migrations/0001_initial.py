# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0001_initial'),
        ('hrm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_day', models.PositiveIntegerField(default=0, null=True, verbose_name=b'Day Work', blank=True)),
                ('sick_day', models.PositiveIntegerField(default=0, null=True, verbose_name=b'Day Sick', blank=True)),
                ('alpha_day', models.PositiveIntegerField(default=0, null=True, verbose_name=b'Day Alpha', blank=True)),
                ('leave_day', models.PositiveIntegerField(default=0, null=True, verbose_name=b'Leave Taken', blank=True)),
                ('leave_left', models.PositiveIntegerField(default=0, null=True, verbose_name=b'Leave Left', blank=True)),
                ('ln', models.PositiveIntegerField(default=0, null=True, verbose_name=b'LN', blank=True)),
                ('lp', models.PositiveIntegerField(default=0, null=True, verbose_name=b'LP', blank=True)),
                ('lk', models.PositiveIntegerField(default=0, null=True, verbose_name=b'LK', blank=True)),
                ('l1', models.PositiveIntegerField(default=0, null=True, verbose_name=b'L1', blank=True)),
                ('l2', models.PositiveIntegerField(default=0, null=True, verbose_name=b'L2', blank=True)),
                ('l3', models.PositiveIntegerField(default=0, null=True, verbose_name=b'L3', blank=True)),
                ('l4', models.PositiveIntegerField(default=0, null=True, verbose_name=b'L4', blank=True)),
                ('employee', models.ForeignKey(verbose_name=b'Employee', to='hrm.Employee')),
            ],
            options={
                'verbose_name': 'Attendance Summary',
                'verbose_name_plural': 'Attendance Summary',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
            ],
            options={
                'verbose_name': 'Courses Type',
                'verbose_name_plural': 'Courses Type',
            },
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('base_salary', models.DecimalField(null=True, verbose_name=b'Base Salary', max_digits=12, decimal_places=2, blank=True)),
                ('overtime', models.DecimalField(null=True, verbose_name=b'Overtime/Hrs', max_digits=12, decimal_places=2, blank=True)),
                ('back_pay', models.DecimalField(null=True, verbose_name=b'Back Pay', max_digits=12, decimal_places=2, blank=True)),
                ('base_salary_per_day', models.DecimalField(null=True, verbose_name=b'Salary/Day', max_digits=12, decimal_places=2, blank=True)),
                ('normal_overtime', models.DecimalField(null=True, verbose_name=b'LN Rate', max_digits=12, decimal_places=2, blank=True)),
                ('total', models.DecimalField(null=True, verbose_name=b'Total Salary', max_digits=12, decimal_places=2, blank=True)),
                ('state', django_fsm.FSMField(default=b'DRAFT', max_length=50, choices=[(b'DRAFT', b'DRAFT'), (b'FINAL', b'FINAL'), (b'PAID', b'PAID')])),
                ('contract', models.ForeignKey(verbose_name=b'Employee Contract', to='hrm.EmployeeContract')),
            ],
            options={
                'verbose_name': 'Payroll',
                'verbose_name_plural': 'Payroll',
                'permissions': (('finalize_payroll', 'Can finalize payroll'), ('unfinalize_payroll', 'Can unfinalize payroll'), ('pay_payroll', 'Can pay payroll'), ('audit_payroll', 'Can audit payroll')),
            },
        ),
        migrations.CreateModel(
            name='PayrollDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.DecimalField(null=True, verbose_name=b'Value', max_digits=12, decimal_places=2, blank=True)),
                ('note', models.CharField(max_length=255, verbose_name=b'Note', blank=True)),
                ('payroll', models.ForeignKey(verbose_name=b'Payroll', to='operational.Payroll')),
                ('salary', models.ForeignKey(verbose_name=b'Component', to='hrm.SalaryName')),
            ],
            options={
                'verbose_name': 'Payroll Detail',
                'verbose_name_plural': 'Payroll Details',
            },
        ),
        migrations.CreateModel(
            name='PayrollPeriod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('period', models.CharField(max_length=15, unique=True, null=True, verbose_name=b'Period', blank=True)),
                ('date_create', models.DateField(auto_now_add=True, verbose_name=b'Date Created')),
                ('start_date', models.DateField(verbose_name=b'Start Date')),
                ('end_date', models.DateField(verbose_name=b'End Date')),
                ('state', django_fsm.FSMField(default=b'OPEN', max_length=50, choices=[(b'OPEN', b'OPEN'), (b'CLOSE', b'CLOSE')])),
            ],
            options={
                'verbose_name': 'Payroll Period',
                'verbose_name_plural': 'Payroll Periods',
                'permissions': (('close_period', 'Can close payroll period'),),
            },
        ),
        migrations.CreateModel(
            name='TrainingClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employee', models.ForeignKey(verbose_name=b'Employee', to='hrm.Employee')),
            ],
            options={
                'verbose_name': 'Training Class',
                'verbose_name_plural': 'Training Classes',
            },
        ),
        migrations.CreateModel(
            name='TrainingSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=b'Date')),
                ('has_certificate', models.BooleanField(default=True, verbose_name=b'Certificate')),
                ('presenter', models.CharField(max_length=45, verbose_name=b'Presenter')),
                ('course', models.ForeignKey(verbose_name=b'Courses', to='operational.Course')),
            ],
            options={
                'verbose_name': 'Training Schedule',
                'verbose_name_plural': 'Training Schedule',
            },
        ),
        migrations.CreateModel(
            name='VisitCustomer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visit_date', models.DateField(verbose_name='Visiting Date')),
                ('subject', models.CharField(max_length=255, verbose_name='Visit Subject Title')),
                ('employee', models.ManyToManyField(help_text='Personnels in the field when these visits', to='hrm.Employee', verbose_name='Personnels at Location')),
                ('sales_order_reference', models.ForeignKey(verbose_name='Sales Order', to='crm.SalesOrder', help_text='Sales Order number for referencing to customer')),
            ],
            options={
                'verbose_name': 'Visit Customer Information',
                'verbose_name_plural': 'Visit Customer Information',
            },
        ),
        migrations.CreateModel(
            name='VisitCustomerDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('report', models.CharField(max_length=255, verbose_name='Point Rate Item')),
                ('visit_customer', models.ForeignKey(verbose_name='Customer', to='operational.VisitCustomer')),
            ],
        ),
        migrations.CreateModel(
            name='VisitPointRateItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Point Rated Item',
                'verbose_name_plural': 'Point Rate Item Lists',
            },
        ),
        migrations.AddField(
            model_name='visitcustomerdetail',
            name='visit_point_rate_item',
            field=models.ForeignKey(verbose_name='Point Rate Item', to='operational.VisitPointRateItem'),
        ),
        migrations.AddField(
            model_name='trainingclass',
            name='schedule',
            field=models.ForeignKey(verbose_name=b'Schedule', to='operational.TrainingSchedule'),
        ),
        migrations.AddField(
            model_name='payroll',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name=b'Period', to='operational.PayrollPeriod'),
        ),
        migrations.AddField(
            model_name='payroll',
            name='staff',
            field=models.ForeignKey(verbose_name=b'User Staff', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.ForeignKey(verbose_name=b'Course Type', to='operational.CourseType'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name=b'Period', to='operational.PayrollPeriod'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='staff',
            field=models.ForeignKey(verbose_name=b'User Staff', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='payrolldetail',
            unique_together=set([('payroll', 'salary')]),
        ),
        migrations.AlterUniqueTogether(
            name='payroll',
            unique_together=set([('contract', 'period')]),
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together=set([('employee', 'period')]),
        ),
    ]
