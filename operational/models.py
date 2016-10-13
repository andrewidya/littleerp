from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.core.urlresolvers import reverse
from crm.models import SalesOrder
from hrm.models import Employee, EmployeeContract, SalaryName
# Create your models here.

class VisitCustomer(models.Model):
	visit_date = models.DateField(verbose_name=_('Visiting Date'))
	sales_order_reference = models.ForeignKey(SalesOrder,
											 verbose_name=_('Sales Order'),
											 help_text=_('Sales Order number \
											 	for referencing to customer'))
	employee = models.ManyToManyField(Employee,
									 verbose_name=_('Personnels at Location'),
									 help_text=_('Personnels in the field when\
									 			these visits'))
	subject = models.CharField(verbose_name=_('Visit Subject Title'),
							  max_length=255)

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
	description = models.CharField(verbose_name=_('Description'),
								  max_length=255)

	class Meta:
		verbose_name = 'Point Rated Item'
		verbose_name_plural = 'Point Rate Item Lists'

	def __str__(self):
		return self.name

class VisitCustomerDetail(models.Model):
	visit_point_rate_item = models.ForeignKey(VisitPointRateItem,
											 verbose_name=_('Point Rate Item'))
	visit_customer = models.ForeignKey(VisitCustomer,
									  verbose_name=_('Customer'))
	report = models.CharField(verbose_name=_('Point Rate Item'),
							 max_length=255)

class PayrollPeriod(models.Model):
	period = models.CharField(verbose_name='Period', max_length=15, blank=True,
							 null=True, unique=True)
	date_create = models.DateField(auto_now_add=True)
	start_date = models.DateField()
	end_date = models.DateField()

	class Meta:
		verbose_name = 'Period'
		verbose_name_plural = 'Periods'

	def __str__(self):
		return "Period: {0} - {1}".format(self.start_date, self.end_date)

	def save(self, *args, **kwargs):
		self.period = str(self.end_date.strftime('%Y-%m'))
		super(PayrollPeriod, self).save(args, kwargs)

	@staticmethod
	def autocomplete_search_fields():
		return ('period__icontains',)

class Attendance(models.Model):
	work_day = models.PositiveIntegerField(verbose_name='Day Work', null=True,
										  blank=True)
	sick_day = models.PositiveIntegerField(verbose_name='Day Sick', null=True,
										  blank=True)
	alpha_day = models.PositiveIntegerField(verbose_name='Day Alpha', null=True,
										   blank=True)
	leave_day = models.PositiveIntegerField(verbose_name='Leave Taken', null=True,
										   blank=True)
	leave_left = models.PositiveIntegerField(verbose_name='Leave Left', null=True,
											blank=True)
	employee = models.ForeignKey(Employee, verbose_name='Employee')
	period = models.ForeignKey(PayrollPeriod, verbose_name='Period')

	class Meta:
		verbose_name = 'Attendance Summary'
		verbose_name_plural = 'Attendance Summary'
		unique_together = ('employee', 'period')

	def __str__(self):
		return "{0} - {1}".format(self.period, self.employee)

class Payroll(models.Model):
	contract = models.ForeignKey(EmployeeContract, verbose_name='Employee \
								contract')
	period = models.ForeignKey(PayrollPeriod, verbose_name='Period')
	base_salary = models.DecimalField(max_digits=12, decimal_places=2, null=True,
									 blank=True, verbose_name='Base Salary')
	overtime = models.DecimalField(max_digits=12, decimal_places=2, null=True,
								  blank=True, verbose_name='Overtime/Hrs')
	back_pay = models.DecimalField(max_digits=12, decimal_places=2, null=True,
								  blank=True, verbose_name='Back Pay')
	staff = models.ForeignKey(User, null=True, blank=True, verbose_name='User \
							 Staff')

	class Meta:
		verbose_name = 'Payroll'
		verbose_name_plural = 'Payroll'
		unique_together = ('contract', 'period')

	def __str__(self):
		return str(self.period.period)

	def save(self, *args, **kwargs):
		if self.base_salary is None:
			self.base_salary = self.contract.base_salary
		if self.overtime is None:
			self.overtime = self.contract.base_salary / 173
		super(Payroll, self).save(args, kwargs)

	def detail_url(self):
		change_list_urls = reverse('admin:operational_payrolldetail_changelist')
		return format_html("<a href='{0}?payroll__contract__employee__id__exact={1}'>\
					      Detail</a>",
					      change_list_urls, self.contract.employee.id)
	detail_url.short_description = 'Details'
	detail_url.allow_tags = True

class PayrollDetail(models.Model):
	payroll = models.ForeignKey(Payroll, verbose_name='Payroll')
	salary = models.ForeignKey(SalaryName, verbose_name='Component')
	value = models.DecimalField(max_digits=12, decimal_places=2, null=True,
		                       blank=True, verbose_name='Value')
	note = models.CharField(max_length=255, blank=True, verbose_name='Note')

	class Meta:
		verbose_name = 'Payroll Detail'
		verbose_name_plural = 'Payroll Details'
		unique_together = ('payroll', 'salary')

	def __str__(self):
		return str(self.payroll)

	@property
	def period(self):
		return self.payroll

	@property
	def contract(self):
		return self.payroll.contract.service_related

	@property
	def employee(self):
		return self.payroll.contract.employee
