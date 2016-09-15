from django.db import models
from django.utils.translation import ugettext as _
from hrm.models import Employee
from crm.models import Customer
# Create your models here.


# Training module
class TrainingType(models.Model):
	name = models.CharField(verbose_name=_('Training Name'), max_length=50)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name

class Training(models.Model):
	date = models.DateField()
	subject = models.CharField(verbose_name=_('Training Subject'), max_length=75)
	author = models.CharField(verbose_name=_('Trainer'), max_length=50, blank=True)
	is_certificate = models.BooleanField()
	report = models.TextField(blank=True)
	employee = models.ForeignKey(Employee, verbose_name=_('Attendance Person'))
	customer = models.ForeignKey(Customer)

	class Meta:
		verbose_name = 'Training'

	def __str__(self):
		return self.author

# Customer visiting module
class VisitEvaluationSubject(models.Model):
	name = models.CharField(verbose_name=_('Evaluation Subject'), max_length=50)

	class Meta:
		verbose_name = 'Visit Evaluation Subject'

	def __str__(self):
		return self.name

class Visit(models.Model):
	date = models.DateField()
	customer = models.ForeignKey(Customer)
	visitor = models.CharField(verbose_name=_('Visitor'), max_length=20)
	visit_record = models.ManyToManyField(VisitEvaluationSubject, through='VisitRecord')

class VisitRecord(models.Model):
	visit = models.ForeignKey(Visit)
	visit_evaluation_subject = models.ForeignKey(VisitEvaluationSubject)
	report = models.TextField(verbose_name=_('Visit Report'), blank=True)
