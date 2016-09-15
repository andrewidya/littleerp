from django.db import models
from django.utils.translation import ugettext as _
from hrm.models import Employee
from crm.models import Customer
# Create your models here.

class PayrollPeriod(models.Model):
	date_created = models.DateField()

	def __str__(self):
		return str(self.date_created)

class Payroll(models.Model):
	employee = models.ForeignKey(Employee, verbose_name=_('Employee Name'))
	customer = models.ForeignKey(Customer, verbose_name=_('Customer'))
	period = models.ForeignKey(PayrollPeriod, verbose_name=_('Payrolling Period'))
	increasing_item = models.ManyToManyField('PayrollIncreaseItem', through='PayrollIncreaseDetail')
	decreasing_item = models.ManyToManyField('PayrollDecreaseItem', through='PayrollDecreaseDetail')

	class Meta:
		unique_together = (('employee', 'customer', 'period'))

	def __str__(self):
		return str(self.period)

	def total_increasing_item(self):
		total = 0
		obj = self.payrollincreasedetail_set.all().filter(payroll=self, employee=self.employee, customer=self.customer)
		for i in range(len(obj)):
			total += obj[i].value
		return total

class PayrollDecreaseItem(models.Model):
	name = models.CharField(verbose_name=_('Decreasing Component'), max_length=25)

	def __str__(self):
		return self.name

class PayrollIncreaseItem(models.Model):
	name = models.CharField(verbose_name=_('Increasing Component'), max_length=25)

	def __str__(self):
		return self.name

class PayrollIncreaseDetail(models.Model):
	item = models.ForeignKey(PayrollIncreaseItem, on_delete=models.CASCADE ,related_name='payroll_increase_items')
	payroll = models.ForeignKey(Payroll, on_delete=models.CASCADE)
	value = models.DecimalField(max_digits=15, decimal_places=2)
	employee = models.ForeignKey(Employee, related_name='employee_payroll_increase_detail')
	customer = models.ForeignKey(Customer, related_name='customer_payroll_increase_detail')

	class Meta:
		unique_together = (('employee', 'customer', 'item'))

	def __str__(self):
		return self.item.name

class PayrollDecreaseDetail(models.Model):
	item = models.ForeignKey(PayrollDecreaseItem, on_delete=models.CASCADE, related_name='payroll_decrease_items')
	payroll = models.ForeignKey(Payroll, on_delete=models.CASCADE)
	value = models.DecimalField(max_digits=15, decimal_places=2)
	employee = models.ForeignKey(Employee, related_name='employee_payroll_decrease_detail')
	customer = models.ForeignKey(Customer, related_name='customer_payroll_decrease_detail')

	class Meta:
		unique_together = (('employee', 'customer', 'item'))

	def __str__(self):
		return self.item.name