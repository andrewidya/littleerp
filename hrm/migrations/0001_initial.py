# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualLeave',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.DateField(verbose_name='Year')),
                ('day_allowed', models.SmallIntegerField(null=True, verbose_name='Day Allowed', blank=True)),
                ('remaining_day_allowed', models.SmallIntegerField(null=True, verbose_name='Remainig Days', blank=True)),
                ('last_update', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Employee Annual Leave',
                'verbose_name_plural': 'Employee Annual Leaves',
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
                ('certificate', models.BooleanField()),
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
                ('reg_number', models.CharField(unique=True, max_length=6, verbose_name='Registration Number')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('birth_place', models.CharField(max_length=25, verbose_name='Birth Place')),
                ('birth_date', models.DateField(verbose_name='Birth Date')),
                ('phone_number', models.CharField(max_length=15, null=True, verbose_name='Phone Number', blank=True)),
                ('gender', models.CharField(max_length=1, verbose_name='Gender', choices=[(b'P', b'Perempuan'), (b'L', b'Laki-laki')])),
                ('bank_account', models.CharField(max_length=20, null=True, verbose_name='Bank Account', blank=True)),
                ('religion', models.CharField(max_length=10, verbose_name='Religion', blank=True)),
                ('id_number', models.CharField(max_length=15, null=True, verbose_name='ID Number', blank=True)),
                ('mother_name', models.CharField(max_length=30, verbose_name='Mother Name')),
                ('blood_type', models.CharField(max_length=2, verbose_name='Blood Type', choices=[(b'A', b'A'), (b'B', b'B'), (b'O', b'O'), (b'AB', b'AB')])),
                ('date_of_hire', models.DateField(verbose_name='Date of Hire')),
                ('marital_status', models.CharField(max_length=3, verbose_name='Marital Status', choices=[(b'TK', b'Belum Menikah'), (b'K/0', b'Menikah Anak 0'), (b'K/1', b'Menikah Anak 1'), (b'K/2', b'Menikah Anak 2'), (b'K/3', b'Menikah Anak 3')])),
                ('is_active', models.BooleanField()),
                ('division', models.ForeignKey(verbose_name='Division', blank=True, to='hrm.Division')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employee Lists',
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
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateField()),
                ('employee', models.ForeignKey(to='hrm.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eval_value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationPeriod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evaluation_date', models.DateField()),
                ('period', models.CharField(max_length=50, null=True, blank=True)),
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
                ('day', models.SmallIntegerField()),
                ('employee', models.ForeignKey(to='hrm.Employee')),
            ],
            options={
                'verbose_name': 'Annual Leave Taken',
                'verbose_name_plural': 'Annual Leave Taken Lists',
            },
        ),
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Ex: Medical, Holliday etc', max_length=50, verbose_name='Leave Type')),
            ],
        ),
        migrations.AddField(
            model_name='leavetaken',
            name='leave_type',
            field=models.ForeignKey(to='hrm.LeaveType'),
        ),
        migrations.AddField(
            model_name='evaluationdetail',
            name='eval_item',
            field=models.ForeignKey(to='hrm.EvaluationItem'),
        ),
        migrations.AddField(
            model_name='evaluationdetail',
            name='evaluation',
            field=models.ForeignKey(to='hrm.Evaluation'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_period',
            field=models.ForeignKey(to='hrm.EvaluationPeriod'),
        ),
        migrations.AddField(
            model_name='employee',
            name='job_title',
            field=models.ForeignKey(verbose_name='Job Tittle', blank=True, to='hrm.JobTitle'),
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
    ]
