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
	date_create = models.DateField(auto_now_add=True, verbose_name='Date Created')
	start_date = models.DateField(verbose_name='Start Date')
	end_date = models.DateField(verbose_name='End Date')

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

	def attendance_urls(self):
		# link to attendance admin changelist
		change_list_urls = reverse('admin:operational_attendance_changelist')
		return format_html("<a href='{0}?period__period={1}'>\
					      Detail</a>",
						  change_list_urls, self.period)
	attendance_urls.allow_tags = True
	attendance_urls.short_description = 'Attendance'

	def payroll_urls(self):
		# link to payroll admin changelist
		change_list_urls = reverse('admin:operational_payroll_changelist')
		return format_html("<a href='{0}?period__period={1}'>\
						  Detail</a>",
						  change_list_urls, self.period)
	payroll_urls.allow_tags = True
	payroll_urls.short_description = 'Payroll'

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
	employee = models.ForeignKey(Employee, verbose_name='Employee',
							    limit_choices_to={'is_active': True,
							    	'contract__contract_status': 'ACTIVE'})
	period = models.ForeignKey(PayrollPeriod, verbose_name='Period')

	class Meta:
		verbose_name = 'Attendance Summary'
		verbose_name_plural = 'Attendance Summary'
		unique_together = ('employee', 'period')

	def __str__(self):
		return "{0} - {1}".format(self.period, self.employee)

	def save(self, *args, **kwargs):
		if self.sick_day is None:
			self.sick_day = 0
		if self.alpha_day is None:
			self.alpha_day = 0
		if self.leave_day is None:
			self.leave_day = 0
		if self.leave_left is None:
			self.leave_left = 0
		super(Attendance, self).save(*args, **kwargs)

class Payroll(models.Model):
	contract = models.ForeignKey(EmployeeContract, limit_choices_to={
									'contract_status': 'ACTIVE',
									'employee__is_active': True},
								verbose_name='Employee \
								Contract')
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
			self.overtime = self.base_salary / 173
		super(Payroll, self).save(args, kwargs)

	def detail_url(self):
		"""
		show payroll details url on admin changelist page
		"""
		change_list_urls = reverse('admin:operational_payrolldetail_changelist')
		return format_html("<a href='{0}?payroll__contract__employee__id__exact={1}'>\
					      Detail</a>",
					      change_list_urls, self.contract.employee.id)
	detail_url.short_description = 'Other Salary Detail'
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
