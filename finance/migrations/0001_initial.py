# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0001_initial'),
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invoice_number', models.PositiveIntegerField(verbose_name='Invoice Number')),
                ('state', django_fsm.FSMField(default=b'DRAFT', max_length=50, choices=[(b'DRAFT', b'DRAFT'), (b'ONGOING', b'ONGOING'), (b'CANCEL', b'CANCEL'), (b'PAID', b'PAID')])),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Date Created')),
            ],
            options={
                'verbose_name': 'Invoice',
            },
        ),
        migrations.CreateModel(
            name='InvoiceDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(verbose_name='Amount', max_digits=12, decimal_places=2)),
                ('note', models.TextField(verbose_name=b'Notes', blank=True)),
                ('invoice', models.ForeignKey(verbose_name='Invoice', to='finance.Invoice')),
            ],
            options={
                'verbose_name': 'Invoice Detail',
                'verbose_name_plural': 'Invoice Details',
            },
        ),
        migrations.CreateModel(
            name='InvoicedItemType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Invoiced Item Type',
                'verbose_name_plural': 'Invoiced Item Type',
            },
        ),
        migrations.CreateModel(
            name='InvoiceTransaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(verbose_name='Amount', max_digits=12, decimal_places=2)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Invoice', to='finance.Invoice')),
            ],
            options={
                'verbose_name': 'Financial Transaction',
                'verbose_name_plural': 'Financial Transactions',
            },
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Transaction Type',
                'verbose_name_plural': 'Transaction Types',
            },
        ),
        migrations.CreateModel(
            name='FinalPayrollPeriod',
            fields=[
            ],
            options={
                'verbose_name': 'Payroll Period',
                'proxy': True,
                'verbose_name_plural': 'Payroll Period',
            },
            bases=('operational.payrollperiod',),
        ),
        migrations.CreateModel(
            name='PaidPayroll',
            fields=[
            ],
            options={
                'verbose_name': 'Payroll Payments History',
                'proxy': True,
                'verbose_name_plural': 'Payroll Payments History',
            },
            bases=('operational.payroll',),
        ),
        migrations.CreateModel(
            name='ProcessedPayroll',
            fields=[
            ],
            options={
                'verbose_name': 'Processed Payroll',
                'proxy': True,
                'verbose_name_plural': 'Processed Payroll',
            },
            bases=('operational.payroll',),
        ),
        migrations.AddField(
            model_name='invoicetransaction',
            name='transaction_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Transaction Type', to='finance.TransactionType'),
        ),
        migrations.AddField(
            model_name='invoicedetail',
            name='invoiced_item',
            field=models.ForeignKey(verbose_name='Invoiced Item', to='finance.InvoicedItemType'),
        ),
        migrations.AddField(
            model_name='invoicedetail',
            name='period',
            field=models.ForeignKey(verbose_name='Period', to='operational.PayrollPeriod'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_detail',
            field=models.ManyToManyField(related_name='invoice_detail', through='finance.InvoiceDetail', to='finance.InvoicedItemType'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='sales_order',
            field=models.ForeignKey(verbose_name='Sales Order', to='crm.SalesOrder'),
        ),
        migrations.AlterUniqueTogether(
            name='invoicedetail',
            unique_together=set([('invoiced_item', 'period')]),
        ),
    ]
