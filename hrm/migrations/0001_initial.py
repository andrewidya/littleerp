# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualLeave',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(verbose_name='Year', choices=[(1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032), (2033, 2033), (2034, 2034), (2035, 2035), (2036, 2036), (2037, 2037), (2038, 2038), (2039, 2039), (2040, 2040), (2041, 2041), (2042, 2042), (2043, 2043), (2044, 2044), (2045, 2045), (2046, 2046), (2047, 2047), (2048, 2048), (2049, 2049), (2050, 2050), (2051, 2051), (2052, 2052), (2053, 2053), (2054, 2054), (2055, 2055), (2056, 2056), (2057, 2057), (2058, 2058), (2059, 2059), (2060, 2060), (2061, 2061), (2062, 2062), (2063, 2063), (2064, 2064), (2065, 2065), (2066, 2066), (2067, 2067), (2068, 2068), (2069, 2069), (2070, 2070), (2071, 2071), (2072, 2072), (2073, 2073), (2074, 2074), (2075, 2075), (2076, 2076), (2077, 2077), (2078, 2078), (2079, 2079), (2080, 2080), (2081, 2081), (2082, 2082), (2083, 2083), (2084, 2084), (2085, 2085), (2086, 2086), (2087, 2087), (2088, 2088), (2089, 2089), (2090, 2090)])),
                ('day_allowed', models.SmallIntegerField(null=True, verbose_name='Day Allowed', blank=True)),
                ('remaining_day_allowed', models.SmallIntegerField(null=True, verbose_name='Remainig Days', blank=True)),
                ('last_update', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Annual Leave',
                'verbose_name_plural': 'Annual Leaves',
            },
        ),
        migrations.CreateModel(
            name='BankName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Bank Name')),
            ],
            options={
                'verbose_name': 'Bank',
                'verbose_name_plural': 'Banks',
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Division Name')),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Division',
                'verbose_name_plural': 'Divisions',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.CharField(max_length=2, verbose_name='Grade', choices=[(b'1', b'SD'), (b'2', b'SMP'), (b'3', b'SMA/SMK Sederajat'), (b'4', b'D1'), (b'5', b'D2'), (b'6', b'D3'), (b'7', b'D4/S1'), (b'8', b'S2/Magister Sederajat'), (b'9', b'S3/Doktoral'), (b'10', b'Akademi/Pelatihan')])),
                ('name', models.CharField(max_length=50, verbose_name='Institution Name')),
                ('address', models.CharField(max_length=100, verbose_name='Address', blank=True)),
                ('city', models.CharField(max_length=25, verbose_name='City', blank=True)),
                ('graduation_date', models.DateField()),
                ('certificate', models.BooleanField(default=False)),
                ('certificate_number', models.CharField(max_length=30, verbose_name='Certificate Number', blank=True)),
                ('description', models.CharField(max_length=255, verbose_name='Short Description', blank=True)),
            ],
            options={
                'verbose_name': 'Education',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reg_number', models.CharField(unique=True, max_length=15, verbose_name='Registration Number')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name', blank=True)),
                ('birth_place', models.CharField(max_length=25, verbose_name='Birth Place')),
                ('birth_date', models.DateField(verbose_name='Birth Date')),
                ('phone_number', models.CharField(max_length=15, null=True, verbose_name='Phone Number', blank=True)),
                ('gender', models.CharField(blank=True, max_length=1, verbose_name='Gender', choices=[(b'P', b'Perempuan'), (b'L', b'Laki-laki')])),
                ('bank_account', models.CharField(max_length=20, null=True, verbose_name='Bank Account', blank=True)),
                ('religion', models.CharField(max_length=10, verbose_name='Religion', blank=True)),
                ('id_number', models.CharField(max_length=15, null=True, verbose_name='ID Number', blank=True)),
                ('mother_name', models.CharField(max_length=30, verbose_name='Mother Name', blank=True)),
                ('blood_type', models.CharField(blank=True, max_length=2, verbose_name='Blood Type', choices=[(b'A', b'A'), (b'B', b'B'), (b'O', b'O'), (b'AB', b'AB')])),
                ('date_of_hire', models.DateField(verbose_name='Date of Hire')),
                ('marital_status', models.CharField(max_length=3, verbose_name='Marital Status', choices=[(b'TK', b'Belum Menikah'), (b'K/0', b'Menikah Anak 0'), (b'K/1', b'Menikah Anak 1'), (b'K/2', b'Menikah Anak 2'), (b'K/3', b'Menikah Anak 3')])),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('bank', models.ForeignKey(verbose_name='Bank', blank=True, to='hrm.BankName', null=True)),
                ('division', models.ForeignKey(verbose_name='Division', blank=True, to='hrm.Division', null=True)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'permissions': (('hrm_employee_view', 'Can view only'),),
            },
        ),
        migrations.CreateModel(
            name='EmployeeAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('district', models.CharField(max_length=255, verbose_name='District')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('province', models.CharField(max_length=255, verbose_name='province')),
                ('address_status', models.CharField(max_length=8, verbose_name='Description', choices=[(b'KTP', b'KTP'), (b'ASAL', b'ASAL'), (b'DOMISILI', b'DOMISILI')])),
                ('employee', models.ForeignKey(to='hrm.Employee')),
            ],
            options={
                'verbose_name': 'Address Information',
                'verbose_name_plural': 'Address Information',
            },
        ),
        migrations.CreateModel(
            name='EmployeeContract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('contract_status', models.CharField(default=b'ACTIVE', max_length=8, blank=True)),
                ('base_salary', models.DecimalField(null=True, verbose_name='Basic Salary', max_digits=12, decimal_places=2, blank=True)),
                ('reference', models.CharField(max_length=255, blank=True)),
                ('employee', models.ForeignKey(related_name='contract', verbose_name='Employee', to='hrm.Employee')),
                ('service_related', models.ForeignKey(related_name='service_order', verbose_name='Customer Demand Related', to='crm.SalesOrderDetail', help_text='This info related to the service needed by customer as detail sales order')),
            ],
            options={
                'verbose_name': 'Contract',
                'verbose_name_plural': 'Contracts',
            },
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_create', models.DateField(verbose_name='Date Created')),
                ('evaluated_location', models.CharField(max_length=255, verbose_name='Location', blank=True)),
                ('ranking', models.CharField(max_length=6, verbose_name='Ranking')),
                ('employee', models.ForeignKey(verbose_name='Employee Name', to='hrm.Employee')),
            ],
            options={
                'verbose_name': 'Evaluation',
                'verbose_name_plural': 'Evaluations',
            },
        ),
        migrations.CreateModel(
            name='EvaluationDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eval_value', models.PositiveIntegerField(verbose_name='Point Value')),
            ],
            options={
                'verbose_name': 'Evaluation Detail',
                'verbose_name_plural': 'Evaluation Details',
            },
        ),
        migrations.CreateModel(
            name='EvaluationItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Evaluating Item',
                'verbose_name_plural': 'Evaluating Items',
            },
        ),
        migrations.CreateModel(
            name='EvaluationPeriod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evaluation_date', models.DateField(verbose_name='Evaluation Date')),
                ('period', models.CharField(max_length=50, null=True, verbose_name='Period', blank=True)),
            ],
            options={
                'verbose_name': 'Evaluation Period',
            },
        ),
        migrations.CreateModel(
            name='FamilyOfEmployee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('birth_place', models.CharField(max_length=25, verbose_name='Birth Place')),
                ('birth_date', models.DateField()),
                ('id_number', models.CharField(max_length=15, null=True, verbose_name='ID Number', blank=True)),
                ('gender', models.CharField(max_length=1, verbose_name='Gender', choices=[(b'P', b'Perempuan'), (b'L', b'Laki-laki')])),
                ('relationship', models.CharField(max_length=1, verbose_name='Relationship', choices=[(b'I', b'Istri'), (b'S', b'Suami'), (b'A', b'Anak')])),
                ('activity', models.CharField(max_length=50, null=True, verbose_name='Current Activity', blank=True)),
                ('employee', models.ForeignKey(to='hrm.Employee')),
            ],
            options={
                'verbose_name': 'Family Information',
                'verbose_name_plural': 'Familiy Informations',
            },
        ),
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Job Title')),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Job Title',
                'verbose_name_plural': 'Job Titles',
            },
        ),
        migrations.CreateModel(
            name='LeaveTaken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('day', models.SmallIntegerField(null=True, blank=True)),
                ('employee', models.ForeignKey(to='hrm.Employee')),
            ],
            options={
                'verbose_name': 'Leave Check List',
                'verbose_name_plural': 'Leave Check Lists',
            },
        ),
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Ex: Medical, Holliday etc', max_length=50, verbose_name='Leave Type')),
            ],
            options={
                'verbose_name': 'Leave Type',
                'verbose_name_plural': 'Leave Types',
            },
        ),
        migrations.CreateModel(
            name='OtherSalary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.DecimalField(verbose_name='Value', max_digits=12, decimal_places=2)),
                ('employee_contract', models.ForeignKey(related_name='other_salary', verbose_name='Employee Contract', to='hrm.EmployeeContract')),
            ],
            options={
                'verbose_name_plural': 'Other Salaries',
            },
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
                ('calculate_condition', models.CharField(help_text='Condition needed for calculate total salary', max_length=1, verbose_name='Calculating Condition', choices=[(b'+', b'Adding Total Salary'), (b'-', b'Decreasing Total Salary')])),
                ('salary_category', models.ForeignKey(related_name='salary_category', on_delete=django.db.models.deletion.PROTECT, to='hrm.SalaryCategory')),
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
        migrations.AddField(
            model_name='leavetaken',
            name='leave_type',
            field=models.ForeignKey(to='hrm.LeaveType'),
        ),
        migrations.AddField(
            model_name='evaluationdetail',
            name='eval_item',
            field=models.ForeignKey(verbose_name='Point Item', to='hrm.EvaluationItem'),
        ),
        migrations.AddField(
            model_name='evaluationdetail',
            name='evaluation',
            field=models.ForeignKey(to='hrm.Evaluation'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_period',
            field=models.ForeignKey(verbose_name='Period', to='hrm.EvaluationPeriod'),
        ),
        migrations.AddField(
            model_name='employee',
            name='job_title',
            field=models.ForeignKey(verbose_name='Job Tittle', blank=True, to='hrm.JobTitle', null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='employee',
            field=models.ForeignKey(to='hrm.Employee'),
        ),
        migrations.AddField(
            model_name='annualleave',
            name='employee',
            field=models.ForeignKey(to='hrm.Employee'),
        ),
        migrations.AddField(
            model_name='annualleave',
            name='leave_type',
            field=models.ForeignKey(to='hrm.LeaveType'),
        ),
        migrations.AlterUniqueTogether(
            name='othersalary',
            unique_together=set([('employee_contract', 'salary_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='evaluationdetail',
            unique_together=set([('evaluation', 'eval_item')]),
        ),
    ]
