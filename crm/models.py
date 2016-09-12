from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class Customer(models.Model):
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
			('view_customer', 'Can view available customer'),
		)

	def __str__(self):
		return self.name

class Branch(models.Model):
	customer = models.ForeignKey(Customer, verbose_name=_('Head Office'))
	code = models.CharField(verbose_name=_('Code'), max_length=10)
	name = models.CharField(verbose_name=_('Name'), max_length=50)
	phone_number = models.CharField(verbose_name=_('Phone Number'), max_length=15, null=True, blank=True)
	address = models.CharField(verbose_name=_('Address'), max_length=100, blank=True)
	city = models.CharField(verbose_name=_('City'), max_length=50, blank=True)

	class Meta:
		verbose_name = 'Customer Branch Office'
		verbose_name_plural = 'Customer Branch Offices'
		permissions = (
			('view_branch', 'Can view available branch'),
		)

	def __str__(self):
		return self.name