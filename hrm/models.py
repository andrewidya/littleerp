from django.db import models
from django.utils.translation import ugettext as _
from crm.models import Customer

# Create your models here.

class Division(models.Model):
	name = models.CharField(verbose_name=_('Division Name'), max_length=20)
	description = models.TextField(blank=True)

	class Meta:
		verbose_name = 'Division'
		verbose_name_plural = 'Divisions'

	def __str__(self):
		return self.name

class JobTitle(models.Model):
	name = models.CharField(verbose_name=_('Job Title'), max_length=20)
	description = models.TextField(blank=True)

	class Meta:
		verbose_name = 'Job Title'
		verbose_name_plural = 'Job Titles'

	def __str__(self):
		return self.name

class MaritalStatus(models.Model):
	code = models.CharField(verbose_name=_('Marital Code'), max_length=4)
	description = models.CharField(verbose_name=_('Description'), max_length=255, blank=True)

	class Meta:
		verbose_name = 'Marital Status'
		verbose_name_plural = 'Marital Statuses'

	def __str__(self):
		return self.code

class Employee(models.Model):
	GENDER_CHOICES = (
		('P', 'Perempuan'),
		('L', 'Laki-laki')
	)

	MARITAL_CHOICES = (
		('TK', 'Belum Menikah'),
		('K/0', 'Menikah Anak 0'),
		('K/1', 'Menikah Anak 1'),
		('K/2', 'Menikah Anak 2'),
		('K/3', 'Menikah Anak 3')
	)

	reg_number = models.CharField(verbose_name=_('Registration Number'), max_length=6, unique=True)
	id_number = models.CharField(verbose_name=_('ID Number'), max_length=15)
	name = models.CharField(verbose_name=_('Name'), max_length=50)
	birth_place = models.CharField(verbose_name=_('Birth Place'), max_length=25)
	birth_date = models.DateField(verbose_name=_('Birth Date'))
	address = models.CharField(verbose_name=_('Address'), max_length=100)
	city = models.CharField(verbose_name=_('City'), max_length=20)
	gender = models.CharField(verbose_name=_('Gender'), max_length=1, choices=GENDER_CHOICES)
	mother_name = models.CharField(verbose_name=_('Mother Name'), max_length=30)
	date_of_hire = models.DateField(verbose_name=_('Date of Hire'))
	bank_account = models.CharField(verbose_name=_('Bank Account'), max_length=20, null=True, blank=True)
	phone_number = models.CharField(verbose_name=_('Phone Number'), max_length=15, null=True, blank=True)
	is_active = models.BooleanField()
	division = models.ForeignKey(Division)
	job_title = models.ForeignKey(JobTitle)
	marital_status = models.CharField(verbose_name=_('Status Pernikahan'), max_length=3, choices=MARITAL_CHOICES)
	salary_information = models.ManyToManyField('SalaryItem', through='SalaryInformation')

	class Meta:
		verbose_name = 'Employee'
		verbose_name_plural = 'Employee Lists'

	def __str__(self):
		return self.name

class FamilyOfEmployee(models.Model):
	GENDER_CHOICES = (
		('P', 'Perempuan'),
		('L', 'Laki-laki')
	)

	RELATIONSHIP_CHOICES = (
		('I', 'Istri'),
		('S', 'Suami'),
		('A', 'Anak'),
	)
	employee = models.ForeignKey(Employee)
	name = models.CharField(verbose_name=_('Name'), max_length=50)
	birth_place = models.CharField(verbose_name=_('Birth Place'), max_length=25)
	birth_date = models.DateField()
	gender = models.CharField(verbose_name=_('Gender'), max_length=1, choices=GENDER_CHOICES)
	relationship = models.CharField(verbose_name=_('Relationship'), max_length=1, choices=RELATIONSHIP_CHOICES)
	current_activity = models.CharField(verbose_name=_('Current Activity'), max_length=50, null=True, blank=True)

	class Meta:
		verbose_name = 'Family Information'
		verbose_name_plural = "Familiy Informations"

	def __str__(self):
		return self.employee.name

# Education Module
class Education(models.Model):
	GRADE_CHOICES = (
		('1', 'SD'),
		('2', 'SMP'),
		('3', 'SMA/SMK Sederajat'),
		('4', 'D1'),
		('5', 'D2'),
		('6', 'D3'),
		('7', 'D4/S1'),
		('8', 'S2/Magister Sederajat'),
		('9', 'S3/Doktoral'),
		('10', 'Akademi/Pelatihan'),
	)

	grade = models.CharField(verbose_name=_('Grade'), max_length=2, choices=GRADE_CHOICES)
	name = models.CharField(verbose_name=_('Institution Name'), max_length=50)
	address = models.CharField(verbose_name=_('Address'), max_length=100, blank=True)
	city = models.CharField(verbose_name=_('City'), max_length=25, blank=True)
	graduation_date = models.DateField()
	certificate_number = models.CharField(verbose_name=_('Certificate Number'), max_length=30, blank=True)
	description = models.CharField(verbose_name=_('Short Description'), max_length=255, blank=True)
	employee = models.ForeignKey(Employee)

	class Meta:
		verbose_name = 'Education'

	def __str__(self):
		return ": " + Education.GRADE_CHOICES[int(self.grade)-1][1]

# Evaluation Module
class EvaluationPeriod(models.Model):
	evaluation_date = models.DateField()
	period = models.CharField(max_length=50, blank=True, null=True)

	class Meta:
		verbose_name = 'Evaluation Period'

	def __str__(self):
		return str(self.evaluation_date)

class EvaluationItem(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=50)
	description = models.TextField(blank=True)
	evaluation = models.ManyToManyField(Employee, through='Evaluation')

	def __str__(self):
		return self.name

class Evaluation(models.Model):
	item = models.ForeignKey(EvaluationItem, related_name='evaluated_item')
	employee = models.ForeignKey(Employee)
	value = models.CharField(verbose_name=_('Value'), max_length=3)
	period = models.ForeignKey(EvaluationPeriod)

	def __str__(self):
		return self.employee.name

# Leave Module
class LeaveRecord(models.Model):
	date_taken = models.DateField(verbose_name=_('Leave Date Taken'))
	employee = models.ForeignKey(Employee)
	customer = models.ForeignKey(Customer)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.employee.name

class SalaryItem(models.Model):
	name = models.CharField(verbose_name=_('Salary Component Name'), max_length=25)
	description = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.name


class SalaryInformation(models.Model):
	salary_item = models.ForeignKey(SalaryItem, on_delete=models.CASCADE)
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	value = models.DecimalField(max_digits=15, decimal_places=2)

	class Meta:
		unique_together = (('salary_item', 'employee'))

	def __str__(self):
		return self.salary_item.name