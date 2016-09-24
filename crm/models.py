from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

# Create your models here.
class Customer(models.Model):
	parent = models.ForeignKey('self', null=True, blank=True, verbose_name=_('Head Office'))
	code = models.CharField(verbose_name=_('Code'), max_length=10, unique=True)
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

	def get_absolute_url(self):
		return reverse('customer-detail', kwargs={'pk': self.pk})

class Service(models.Model):
	name = models.CharField(verbose_name=_('Service Provided'), max_length=255)

	class Meta:
		verbose_name = 'Service Provided'
		verbose_name = 'Service Provided List'

	def __str__(self):
		return self.name

class SalesOrder(models.Model):
	FEE_CONDITION_CHOICES = (
		('BASIC', 'Basic Salary'),
		('TOTAL', 'Grand Total')
	)
	number = models.CharField(verbose_name=_('SO Number'), max_length=50, blank=True)
	date_create = models.DateField(verbose_name=_('Date Issued'))
	date_start = models.DateField(verbose_name=_('Contract Start Date'))
	date_end = models.DateField(verbose_name=_('Contract End Date'))
	customer = models.ForeignKey(Customer, verbose_name=_('Customer Name'))
	reference = models.CharField(verbose_name=_('Reference'), max_length=255, blank=True)
	note = models.TextField(blank=True)
	tax = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_('Tax'), help_text=_('Tax value must be decimal, ex: input 12\% / as 0.12'))
	fee = models.DecimalField(max_digits=12, decimal_places=3, verbose_name=_('Management Fee'))
	fee_calculate_condition = models.CharField(verbose_name=_('Fee Calculated Condition'), help_text=_('Set to basic if the fee will be calculated \
		from basic salary, otherwise set to grand total'), max_length=5, choices=FEE_CONDITION_CHOICES)

	class Meta:
		verbose_name = 'Sales Order'
		verbose_name_plural = 'Sales Orders'

	def __str__(self):
		return self.number

	def save(self, *args, **kwargs):
		if self.id == None:
			from datetime import datetime
			date = datetime.now().strftime("%Y%m%d")
			self.number = "SO" + date
		super(SalesOrder, self).save(*args, **kwargs)

class SalesOrderDetail(models.Model):
	sales_order = models.ForeignKey(SalesOrder, verbose_name=_('Sales Order Number'))
	service = models.ForeignKey(Service, verbose_name=_('Service Demand'))
	quantity = models.SmallIntegerField(verbose_name=_('Unit Quantity'))
	basic_salary = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
	other_salary_detail = models.ManyToManyField('ServiceSalaryItem', through='ServiceSalaryDetail', related_name='other_salary_detail')

	class Meta:
		verbose_name = 'Sales Order Detail'
		verbose_name_plural = 'Sales Order Details'

	def __str__(self):
		return self.sales_order.number + ":" + self.service.name

class ItemCategory(models.Model):
	name = models.CharField(verbose_name=_('Item Category'), max_length=255)

	class Meta:
		verbose_name = 'Item Category'
		verbose_name_plural = 'Item Categories'

	def __str__(self):
		return self.name

class ServiceSalaryItem(models.Model):
	name = models.CharField(verbose_name=_('Price Item Component'), max_length=255)
	category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, verbose_name=_('Category'), related_name='service_price_item')

	class Meta:
		verbose_name = 'Service Salary Item'
		verbose_name_plural = 'Service Salary Items'

	def __str__(self):
		return self.name

class ServiceSalaryDetail(models.Model):
	service_order_detail = models.ForeignKey(SalesOrderDetail, verbose_name=_('Service Order Detail'), on_delete=models.CASCADE)
	service_salary_item = models.ForeignKey(ServiceSalaryItem, verbose_name=_('Salary Item'), on_delete=models.CASCADE)
	price = models.DecimalField(verbose_name=_('Price'), max_digits=12, decimal_places=2)

	class Meta:
		verbose_name = 'Detail Salary on Service'
		verbose_name_plural = 'Detail Salary on Service'
		unique_together = (('service_order_detail', 'service_salary_item'),)

	def __str__(self):
		return self.service_salary_item.name + ":" + self.service_order_detail.sales_order.number