from django_fsm import FSMField, transition

from django.db import models
from django.db.models import Sum

from operational.models import (Payroll, State, PayrollPeriod, PayrollDetail)
# Create your models here.

class PaidPayrollManager(models.Manager):
	def get_queryset(self):
		return super(PaidPayrollManager, self).get_queryset().filter(
					models.Q(state=State.PAID))


class ProcessedPayrollManager(models.Manager):
	def get_queryset(self):
		return super(ProcessedPayrollManager, self).get_queryset().filter(models.Q(state=State.FINAL) | models.Q(state=State.PAID))


class FinalPayrollManager(models.Manager):
	def get_queryset(self):
		return super(FinalPayrollManager, self).get_queryset().annotate(total_payment=Sum('payroll__total'))


class PaidPayroll(Payroll):
	objects = PaidPayrollManager()

	class Meta:
		proxy = True
		verbose_name = 'Payroll Payments History'
		verbose_name_plural = 'Payroll Payments History'


class ProcessedPayroll(Payroll):
	objects = ProcessedPayrollManager()

	class Meta:
		proxy = True
		verbose_name = 'Processed Payroll'
		verbose_name_plural = 'Processed Payroll'

	def employee(self):
		return str(self.contract.employee)


class FinalPayrollPeriod(PayrollPeriod):
	objects = FinalPayrollManager()

	class Meta:
		proxy = True
		verbose_name = 'Payroll Period'
		verbose_name_plural = 'Payroll Period'

	def total(self):
		return self.total_payment
	total.short_description = 'Total Payroll'