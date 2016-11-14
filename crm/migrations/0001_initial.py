# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=10, verbose_name='Code')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('phone_number', models.CharField(max_length=15, null=True, verbose_name='Phone Number', blank=True)),
                ('address', models.CharField(max_length=100, verbose_name='Address', blank=True)),
                ('city', models.CharField(max_length=50, verbose_name='City', blank=True)),
                ('field', models.CharField(max_length=20, verbose_name='Field', blank=True)),
                ('logo', models.ImageField(upload_to=b'crm/customer/logo/%Y/%m/%d', null=True, verbose_name=b'Logo', blank=True)),
                ('tax_id_number', models.CharField(max_length=30, verbose_name='NPWP', blank=True)),
                ('join_date', models.DateField()),
                ('parent', models.ForeignKey(verbose_name='Head Office', blank=True, to='crm.Customer', null=True)),
            ],
            options={
                'verbose_name': 'Customer List',
                'verbose_name_plural': 'Customer Information',
                'permissions': (('view_only_customer', 'Can view only available customer'),),
            },
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Item Category')),
            ],
            options={
                'verbose_name': 'Salary Category',
                'verbose_name_plural': 'Salary Categories',
            },
        ),
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=50, verbose_name='SO Number', blank=True)),
                ('date_create', models.DateField(verbose_name='Date Issued')),
                ('date_start', models.DateField(verbose_name='Contract Start Date')),
                ('date_end', models.DateField(verbose_name='Contract End Date')),
                ('reference', models.CharField(max_length=255, verbose_name='Reference', blank=True)),
                ('note', models.TextField(blank=True)),
                ('tax', models.DecimalField(help_text='Tax value must be decimal, ex: input 12\\% / as 0.12', verbose_name='Tax', max_digits=12, decimal_places=2)),
                ('fee', models.DecimalField(verbose_name='Management Fee', max_digits=12, decimal_places=3)),
                ('fee_calculate_condition', models.CharField(help_text='Set to basic if the fee will be calculated from basic salary, otherwise set to grand total', max_length=5, verbose_name='Fee Calculated Condition', choices=[(b'BASIC', b'Basic Salary'), (b'TOTAL', b'Grand Total')])),
                ('customer', models.ForeignKey(verbose_name='Customer Name', to='crm.Customer')),
            ],
            options={
                'verbose_name': 'Sales Order',
                'verbose_name_plural': 'Sales Orders',
            },
        ),
        migrations.CreateModel(
            name='SalesOrderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.SmallIntegerField(verbose_name='Unit Quantity')),
                ('basic_salary', models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)),
            ],
            options={
                'verbose_name': 'Order Detail',
                'verbose_name_plural': 'Order Details',
            },
        ),
        migrations.CreateModel(
            name='Satisfication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateField(verbose_name='Date Created')),
                ('name', models.CharField(max_length=255, verbose_name='Subject')),
                ('respondent', models.CharField(max_length=50, verbose_name='Person Interviewed', blank=True)),
                ('sales_order', models.ForeignKey(verbose_name='Related Sales Order', to='crm.SalesOrder')),
            ],
            options={
                'verbose_name': 'Satisfication',
                'verbose_name_plural': 'Satisfication Interview',
            },
        ),
        migrations.CreateModel(
            name='SatisficationDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.PositiveIntegerField(help_text='Value must be betwen 2 to 5', verbose_name='Point Value')),
            ],
            options={
                'verbose_name': 'Satisfication Interview Detail',
                'verbose_name_plural': 'Satisfication Interview Details',
            },
        ),
        migrations.CreateModel(
            name='SatisficationPointCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Satisfication Point Category')),
                ('description', models.TextField(verbose_name='Description', blank=True)),
            ],
            options={
                'verbose_name': 'Satisfication Point Category',
                'verbose_name_plural': 'Satisfication Point Categories',
            },
        ),
        migrations.CreateModel(
            name='SatisficationPointRateItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Point rate question for polling', max_length=255, verbose_name='Satisfication Point Rate')),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('category', models.ForeignKey(verbose_name='Point Category', to='crm.SatisficationPointCategory')),
            ],
            options={
                'verbose_name': 'Satisfication Point Rate Item',
                'verbose_name_plural': 'Satisfication Point Rate Item',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Service Provided')),
            ],
            options={
                'verbose_name': 'Service Provided List',
            },
        ),
        migrations.CreateModel(
            name='ServiceSalaryDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(verbose_name='Price', max_digits=12, decimal_places=2)),
                ('service_order_detail', models.ForeignKey(verbose_name='Service Order Detail', to='crm.SalesOrderDetail')),
            ],
            options={
                'verbose_name': 'Detail Salary Per Service',
                'verbose_name_plural': 'Detail Salary Per Service',
            },
        ),
        migrations.CreateModel(
            name='ServiceSalaryItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Price Item Component')),
                ('category', models.ForeignKey(related_name='service_price_item', verbose_name='Category', to='crm.ItemCategory')),
            ],
            options={
                'verbose_name': 'Service Salary Item',
                'verbose_name_plural': 'Service Salariy Items',
            },
        ),
        migrations.AddField(
            model_name='servicesalarydetail',
            name='service_salary_item',
            field=models.ForeignKey(verbose_name='Salary Item', to='crm.ServiceSalaryItem'),
        ),
        migrations.AddField(
            model_name='satisficationdetail',
            name='point_rate_item',
            field=models.ForeignKey(verbose_name='Point Rate Item', to='crm.SatisficationPointRateItem'),
        ),
        migrations.AddField(
            model_name='satisficationdetail',
            name='satisfication',
            field=models.ForeignKey(verbose_name='Satisfication Subject', to='crm.Satisfication'),
        ),
        migrations.AddField(
            model_name='salesorderdetail',
            name='other_salary_detail',
            field=models.ManyToManyField(related_name='other_salary_detail', through='crm.ServiceSalaryDetail', to='crm.ServiceSalaryItem'),
        ),
        migrations.AddField(
            model_name='salesorderdetail',
            name='sales_order',
            field=models.ForeignKey(verbose_name='Sales Order Number', to='crm.SalesOrder'),
        ),
        migrations.AddField(
            model_name='salesorderdetail',
            name='service',
            field=models.ForeignKey(verbose_name='Service Demand', to='crm.Service'),
        ),
        migrations.AlterUniqueTogether(
            name='servicesalarydetail',
            unique_together=set([('service_order_detail', 'service_salary_item')]),
        ),
        migrations.AlterUniqueTogether(
            name='satisficationdetail',
            unique_together=set([('satisfication', 'point_rate_item')]),
        ),
    ]
