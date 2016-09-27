from django.db import models
from django.utils.translation import ugettext as _
from crm.models import SalesOrder
from hrm.models import Employee
# Create your models here.

class VisitCustomer(models.Model):
	visit_date = models.DateField(verbose_name=_('Visiting Date'))
	sales_order_reference = models.ForeignKey(SalesOrder, verbose_name=_('Sales Order'), help_text=_('Sales Order number for referencing to customer'))
	employee = models.ManyToManyField(Employee, verbose_name=_('Personnels at Location'), help_text=_('Personnels in the field when these visits'))
	subject = models.CharField(verbose_name=_('Visit Subject Title'), max_length=255)

	class Meta:
		verbose_name = 'Visit Customer Information'
		verbose_name_plural = 'Visit Customer Information'

	def __str__(self):
		return self.sales_order_reference.number

	def get_customer_name(self):
		return self.sales_order_reference.customer

	get_customer_name.short_description = 'Customer'

class VisitPointRateItem(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=50)
	description = models.CharField(verbose_name=_('Description'), max_length=255)

	class Meta:
		verbose_name = 'Point Rated Item'
		verbose_name_plural = 'Point Rate Item Lists'

	def __str__(self):
		return self.name

class VisitCustomerDetail(models.Model):
	visit_point_rate_item = models.ForeignKey(VisitPointRateItem, verbose_name=_('Point Rate Item'))
	visit_customer = models.ForeignKey(VisitCustomer, verbose_name=_('Customer'))
	report = models.CharField(verbose_name=_('Point Rate Item'), max_length=255)


