from django.db import models
from operational.models import Payroll, State
# Create your models here.

class PaidPayrollManager(models.Manager):
	def get_queryset(self):
		return super(PaidPayrollManager, self).get_queryset().filter(
					models.Q(state=State.PAID))

class PaidPayroll(Payroll):
	objects = PaidPayrollManager()
	class Meta:
		proxy = True
		verbose_name = 'Payroll Payments History'
		verbose_name_plural = 'Payroll Payments History'