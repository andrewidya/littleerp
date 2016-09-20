from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
class Customer(models.Model):
	parent = models.ForeignKey('self', null=True, blank=True, verbose_name=_('Head Office'))
	code = models.CharField(verbose_name=_('Code'), max_length=10)
	name = models.CharField(verbose_name=_('Name'), max_length=50)
	phone_number = models.CharField(verbose_name=_('Phone Number'), max_length=15, null=True, blank=True)
	address = models.CharField(verbose_name=_('Address'), max_length=100, blank=True)
	city = models.CharField(verbose_name=_('City'), max_length=50, blank=True)
	field = models.CharField(verbose_name=_('Field'), max_length=20, blank=True)
	# logo = models.ImageField()
	tax_id_number = models.CharField(verbose_name=_('NPWP'), max_length=30, blank=True)
	join_date = models.DateField()

	class Meta:
		verbose_name = 'Customer List'
		verbose_name_plural = 'Customer Information'
		permissions = (
			('view_only_customer', 'Can view only available customer'),
		)

	def __str__(self):
		return self.name

class SalesOrder(models.Model):
	FEE_CONDITION_CHOICES = (
		('BASIC', 'Basic Salary'),
		('TOTAL', 'Grand Total')
	)
	number = models.CharField(verbose_name=_('SO Number'), max_length=50)
	date_create = models.DateField(verbose_name=_('Date Issued'))
	date_start = models.DateField(verbose_name=_('Contract Start Date'))
	date_end = models.DateField(verbose_name=_('Contract End Date'))
	customer = models.ForeignKey(Customer, verbose_name=_('Customer Name'))
	reference = models.CharField(verbose_name=_('Reference'), max_length=255)
	note = models.TextField()
	tax = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_('Tax'), help_text=_('Tax value must be decimal, ex: input 12\% / as 0.12'))
	fee = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_('Management Fee'))
	fee_calculate_condition = models.CharField(verbose_name=_('Fee Calculated Condition'), help_text=_('Set to basic if the fee will be calculated \
		from basic salary, otherwise set to grand total'), max_length=5, choices=FEE_CONDITION_CHOICES)

	class Meta:
		verbose_name = 'Sales Order'
		verbose_name_plural = 'Sales Orders'

	def __str__(self):
		return self.number
