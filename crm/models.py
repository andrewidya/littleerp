from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

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
		return self.number + " : " + self.customer.name

	def save(self, *args, **kwargs):
		if self.id == None:
			from datetime import datetime
			date = datetime.now().strftime("%Y%m%d")
			self.number = "SO" + date
		super(SalesOrder, self).save(*args, **kwargs)

	def service_demand_list(self):
		sales_order_detail = self.salesorderdetail_set.all().filter(sales_order=self)
		service = []
		for s in sales_order_detail:
			service.append(s.service.name)
		return str(service)

	@property
	def total_price(self):
		total = 0
		sales_order_detail = self.salesorderdetail_set.all().filter(sales_order=self)
		for service in sales_order_detail:
			service_price = 0
			salary = 0
			print("Beginning")
			print("Salary: --------" + str(salary))
			print("After calculated:")
			for service_salary in service.servicesalarydetail_set.all():
				salary += service_salary.price
				print("Salary: " + str(salary))
				print("Service Price: " +  str(service_price))
			service_price = salary + service.basic_salary
			print("Total:")
			print("Service Price: " + str(service_price))
			total += service_price * service.quantity

		return 'IDR{:,.2f}'.format(total)

	def sales_order_detail_page(self):
		return mark_safe('<a href="%ssalesorderdetail/?sales_order__number=%s">See Detail</a>' % (reverse('admin:app_list', kwargs={'app_label': 'crm'}), self.number))

	@staticmethod
	def autocomplete_search_fields():
		return ("number__icontains",)

class SalesOrderDetail(models.Model):
	sales_order = models.ForeignKey(SalesOrder, verbose_name=_('Sales Order Number'))
	service = models.ForeignKey(Service, verbose_name=_('Service Demand'))
	quantity = models.SmallIntegerField(verbose_name=_('Unit Quantity'))
	basic_salary = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
	other_salary_detail = models.ManyToManyField('ServiceSalaryItem', through='ServiceSalaryDetail', related_name='other_salary_detail')

	class Meta:
		verbose_name = 'Order Detail'
		verbose_name_plural = 'Order Details'

	def __str__(self):
		return self.sales_order.number + ":" + self.service.name

	def get_service(self):
		return self.service.name

	@staticmethod
	def autocomplete_search_fields():
		return ('sales_order__number__icontains', 'service__name__icontains')

class ItemCategory(models.Model):
	name = models.CharField(verbose_name=_('Item Category'), max_length=255)

	class Meta:
		verbose_name = 'Salary Category'
		verbose_name_plural = 'Salary Categories'

	def __str__(self):
		return self.name

class ServiceSalaryItem(models.Model):
	name = models.CharField(verbose_name=_('Price Item Component'), max_length=255)
	category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, verbose_name=_('Category'), related_name='service_price_item')

	class Meta:
		verbose_name = 'Service Salary Item'
		verbose_name_plural = 'Service Salariy Items'

	def __str__(self):
		return self.name

class ServiceSalaryDetail(models.Model):
	service_order_detail = models.ForeignKey(SalesOrderDetail, verbose_name=_('Service Order Detail'), on_delete=models.CASCADE)
	service_salary_item = models.ForeignKey(ServiceSalaryItem, verbose_name=_('Salary Item'), on_delete=models.CASCADE)
	price = models.DecimalField(verbose_name=_('Price'), max_digits=12, decimal_places=2)

	class Meta:
		verbose_name = 'Detail Salary Per Service'
		verbose_name_plural = 'Detail Salary Per Service'
		unique_together = (('service_order_detail', 'service_salary_item'),)

	def __str__(self):
		return self.service_salary_item.name + ":" + self.service_order_detail.sales_order.number