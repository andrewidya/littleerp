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

class Employee(models.Model):
	BLODD_TYPE_CHOICES = (
		('A', 'A'),
		('B', 'B'),
		('O', 'O'),
		('AB', 'AB')
	)

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
	first_name = models.CharField(verbose_name=_('First Name'), max_length=50)
	last_name = models.CharField(verbose_name=_('Last Name'), max_length=50)
	birth_place = models.CharField(verbose_name=_('Birth Place'), max_length=25)
	birth_date = models.DateField(verbose_name=_('Birth Date'))
	phone_number = models.CharField(verbose_name=_('Phone Number'), max_length=15, null=True, blank=True)
	gender = models.CharField(verbose_name=_('Gender'), max_length=1, choices=GENDER_CHOICES)
	bank_account = models.CharField(verbose_name=_('Bank Account'), max_length=20, null=True, blank=True)
	religion = models.CharField(verbose_name=_('Religion'), max_length=10, blank=True)	
	id_number = models.CharField(verbose_name=_('ID Number'), max_length=15, null=True, blank=True)
	job_title = models.ForeignKey(JobTitle, verbose_name=_('Job Tittle'), blank=True)
	division = models.ForeignKey(Division, verbose_name=_('Division'), blank=True)
	mother_name = models.CharField(verbose_name=_('Mother Name'), max_length=30)
	blood_type = models.CharField(verbose_name=_('Blood Type'), max_length=2, choices=BLODD_TYPE_CHOICES)
	date_of_hire = models.DateField(verbose_name=_('Date of Hire'))
	marital_status = models.CharField(verbose_name=_('Marital Status'), max_length=3, choices=MARITAL_CHOICES)	
	is_active = models.BooleanField()

	class Meta:
		verbose_name = 'Employee'
		verbose_name_plural = 'Employee Lists'

	def __str__(self):
		return self.name

class EmployeeAddress(models.Model):
	employee = models.ForeignKey(Employee)
	address = models.CharField(verbose_name=_('Address'), max_length=255)
	district = models.CharField(verbose_name=_('District'), max_length=255)
	city = models.CharField(verbose_name=_('City'), max_length=255)
	province = models.CharField(verbose_name=_('province'), max_length=255)
	address_status = models.CharField(verbose_name=_('Description'), max_length=8, choices=(('KTP', 'KTP'), ('ASAL', 'ASAL'), ('DOMISILI', 'DOMISILI')))

	def __str__(self):
		return self.address

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
	id_number = models.CharField(verbose_name=_('ID Number'), max_length=15, null=True, blank=True)
	gender = models.CharField(verbose_name=_('Gender'), max_length=1, choices=GENDER_CHOICES)
	relationship = models.CharField(verbose_name=_('Relationship'), max_length=1, choices=RELATIONSHIP_CHOICES)
	activity = models.CharField(verbose_name=_('Current Activity'), max_length=50, null=True, blank=True)

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

	employee = models.ForeignKey(Employee)
	grade = models.CharField(verbose_name=_('Grade'), max_length=2, choices=GRADE_CHOICES)
	name = models.CharField(verbose_name=_('Institution Name'), max_length=50)
	address = models.CharField(verbose_name=_('Address'), max_length=100, blank=True)
	city = models.CharField(verbose_name=_('City'), max_length=25, blank=True)
	graduation_date = models.DateField()
	certificate = models.BooleanField()
	certificate_number = models.CharField(verbose_name=_('Certificate Number'), max_length=30, blank=True)
	description = models.CharField(verbose_name=_('Short Description'), max_length=255, blank=True)	

	class Meta:
		verbose_name = 'Education'

	def __str__(self):
		return ": " + Education.GRADE_CHOICES[int(self.grade)-1][1]

# Leave Module
class LeaveType(models.Model):
	name = models.CharField(verbose_name=_('Leave Type'), max_length=50, help_text="Ex: Medical, Holliday etc")

	class Meta:
		verbose_name = 'Leave Type'
		verbose_name_plural = 'Leave Types'

	def __str__(self):
		return self.name

class AnnualLeave(models.Model):
	employee = models.ForeignKey(Employee)
	leave_type = models.ForeignKey(LeaveType)
	year = models.DateField(verbose_name=_('Year'));
	day_allowed = models.SmallIntegerField(verbose_name=_('Day Allowed'), null=True, blank=True)
	remaining_day_allowed = models.SmallIntegerField(verbose_name=_('Remainig Days'), null=True, blank=True)
	last_update = models.DateField(auto_now_add=True)
	
	class Meta:
		verbose_name = 'Employee Annual Leave'
		verbose_name_plural = 'Employee Annual Leaves'

	def __str__(self):
		return self.employee.name

class LeaveTaken(models.Model):
	employee = models.ForeignKey(Employee)
	leave_type = models.ForeignKey(LeaveType)
	from_date = models.DateField()
	to_date = models.DateField()
	day = models.SmallIntegerField()

	class Meta:
		verbose_name = 'Annual Leave Taken'
		verbose_name_plural = 'Annual Leave Taken Lists'

	def __str__(self):
		return self.employee.name

	def save(self, *args, **kwargs):
		diff = self.to_date - self.from_date
		self.day = diff.days
		super(LeaveType, self).save(*args, **kwargs)

# Evaluation Module
class EvaluationPeriod(models.Model):
	evaluation_date = models.DateField()
	period = models.CharField(max_length=50, blank=True, null=True)

	class Meta:
		verbose_name = 'Evaluation Period'

	def __str__(self):
		return str(self.evaluation_date)

	def save(self, *args, **kwargs):
		if self.id == None:
			self.period = str(self.evaluation_date.month) + "-" + str(self.evaluation_date.year)
		super(EvaluationPeriod, self).save(*args, **kwargs)

class EvaluationItem(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=50)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name

class Evaluation(models.Model):
	employee = models.ForeignKey(Employee)
	eval_period = models.ForeignKey(EvaluationPeriod)
	date_created = models.DateField()


class EvaluationDetail(models.Model):
	evaluation = models.ForeignKey(Evaluation)
	eval_item = models.ForeignKey(EvaluationItem)
	eval_value = models.TextField()