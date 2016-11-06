from __future__ import division
from decimal import Decimal

from django_fsm import FSMField, transition

from django.db import models
from django.db.models import Sum, Q
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.core.urlresolvers import reverse

from crm.models import SalesOrder
from hrm.models import Employee, EmployeeContract, SalaryName
# Create your models here.

class FinalPayrollManager(models.Manager):
	def get_queryset(self):
		return super(FinalPayrollManager, self).get_queryset().filter(models.Q(state=State.FINAL))


class PayrollManager(models.Manager):
	def get_queryset(self):
		return super(PayrollManager, self).get_queryset().filter(state=State.DRAFT).select_related('contract__employee')


class State(object):
    '''
    Constants to represent the `state`s of the PublishableModel
    '''
    DRAFT = 'DRAFT'
    FINAL = 'FINAL'
    PAID = 'PAID'
    OPEN = 'OPEN'
    CLOSE = 'CLOSE'

    CHOICES = (
        (DRAFT, DRAFT),
        (FINAL, FINAL),
        (PAID, PAID),
        (OPEN, OPEN),
        (CLOSE, CLOSE),
    )


class VisitCustomer(models.Model):
	visit_date = models.DateField(verbose_name=_('Visiting Date'))
	sales_order_reference = models.ForeignKey(
		SalesOrder, verbose_name=_('Sales Order'),
		help_text=_('Sales Order number for referencing to customer'))
	employee = models.ManyToManyField(
		Employee, verbose_name=_('Personnels at Location'),
		help_text=_('Personnels in the field when these visits'))
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


class PayrollPeriod(models.Model):
	period = models.CharField(
		verbose_name='Period',
		max_length=15,
		blank=True,
		null=True,
		unique=True,
	)
	date_create = models.DateField(auto_now_add=True, verbose_name='Date Created')
	start_date = models.DateField(verbose_name='Start Date')
	end_date = models.DateField(verbose_name='End Date')
	state = FSMField(default=State.OPEN, choices=State.CHOICES)

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
		return format_html("<a href='{0}?period__period={1}'>Detail</a>",
						  change_list_urls, self.period)
	attendance_urls.allow_tags = True
	attendance_urls.short_description = 'Attendance'

	@transition(field=state, source=State.OPEN, target=State.CLOSE)
	def close(self):
		pass

	def payroll_urls(self):
		# link to payroll admin changelist
		change_list_urls = reverse('admin:operational_payroll_changelist')
		return format_html("<a href='{0}?period__period={1}'>\
						  Detail</a>",
						  change_list_urls, self.period)
	payroll_urls.allow_tags = True
	payroll_urls.short_description = 'Payroll'


class Attendance(models.Model):
	work_day = models.PositiveIntegerField(verbose_name='Day Work', null=True, blank=True)
	sick_day = models.PositiveIntegerField(verbose_name='Day Sick', null=True, blank=True, default=0)
	alpha_day = models.PositiveIntegerField(verbose_name='Day Alpha', null=True, blank=True, default=0)
	leave_day = models.PositiveIntegerField(verbose_name='Leave Taken', null=True, blank=True, default=0)
	leave_left = models.PositiveIntegerField(verbose_name='Leave Left', null=True, blank=True, default=0)
	ln = models.PositiveIntegerField(verbose_name='LN', null=True, blank=True, default=0)
	lp = models.PositiveIntegerField(verbose_name='LP', null=True, blank=True, default=0)
	lk = models.PositiveIntegerField(verbose_name='LK', null=True, blank=True, default=0)
	l1 = models.PositiveIntegerField(verbose_name='L1', null=True, blank=True, default=0)
	l2 = models.PositiveIntegerField(verbose_name='L2', null=True, blank=True, default=0)
	l3 = models.PositiveIntegerField(verbose_name='L3', null=True, blank=True, default=0)
	l4 = models.PositiveIntegerField(verbose_name='L4', null=True, blank=True, default=0)
	employee = models.ForeignKey(
		Employee,
		verbose_name='Employee',
		limit_choices_to=(
			Q(is_active=True)
			& (Q(contract__contract_status='ACTIVE')
				| Q(contract__contract_status='NEED RENEWAL'))))
	period = models.ForeignKey(PayrollPeriod, verbose_name='Period', on_delete=models.PROTECT)
	staff = models.ForeignKey(User, null=True, blank=True, verbose_name='User Staff')

	class Meta:
		verbose_name = 'Attendance Summary'
		verbose_name_plural = 'Attendance Summary'
		unique_together = ('employee', 'period')

	def __str__(self):
		return "{0} - {1}".format(self.period, self.employee)

	def save(self, *args, **kwargs):
		'''
		Always save attendance attribute value with 0 instead of None
		'''
		if self.sick_day is None:
			self.sick_day = 0
		if self.alpha_day is None:
			self.alpha_day = 0
		if self.leave_day is None:
			self.leave_day = 0
		if self.leave_left is None:
			self.leave_left = 0
		if self.ln is None:
			self.ln  = 0
		if self.lp is None:
			self.lp  = 0
		if self.lk is None:
			self.lk  = 0
		if self.l1 is None:
			self.l1  = 0
		if self.l2 is None:
			self.l2  = 0
		if self.l3 is None:
			self.l3  = 0
		if self.l4 is None:
			self.l4  = 0
		super(Attendance, self).save(*args, **kwargs)


class Payroll(models.Model):
	contract = models.ForeignKey(
		EmployeeContract,
		limit_choices_to=Q(contract_status='ACTIVE') | Q(contract_status='NEED RENEWAL'),
		verbose_name='Employee Contract')
	period = models.ForeignKey(
		PayrollPeriod,
		verbose_name='Period',
		on_delete=models.PROTECT
	)
	base_salary = models.DecimalField(
		max_digits=12,
		decimal_places=2,
		null=True,
		blank=True,
		verbose_name='Base Salary'
	)
	overtime = models.DecimalField(
		max_digits=12,
		decimal_places=2,
		null=True,
		blank=True,
		verbose_name='Overtime/Hrs')
	back_pay = models.DecimalField(
		max_digits=12,
		decimal_places=2,
		null=True,
		blank=True,
		verbose_name='Back Pay'
	)
	base_salary_per_day = models.DecimalField(
		max_digits=12,
		decimal_places=2,
		null=True,
		blank=True,
		verbose_name='Salary/Day'
	)
	normal_overtime = models.DecimalField(
		max_digits=12,
		decimal_places=2,
		null=True,
		blank=True,
		verbose_name='LN Rate'
	)
	staff = models.ForeignKey(User, null=True, blank=True, verbose_name='User Staff')
	state = FSMField(default=State.DRAFT, choices=State.CHOICES)
	total = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name='Total Salary')

	draft_manager = PayrollManager()
	objects = models.Manager()

	class Meta:
		verbose_name = 'Payroll'
		verbose_name_plural = 'Payroll'
		unique_together = ('contract', 'period')
		permissions = (
			('audit_payroll', 'Can audit payroll'),
		)

	def __str__(self):
		return str(self.period.period)

	def save(self, *args, **kwargs):
		if self.base_salary is None:
			self.base_salary = self.contract.base_salary
			self.overtime = self.base_salary / 173
			self.base_salary_per_day = self.base_salary / 30
		if self.back_pay is None:
			self.back_pay = 0
		if self.total is None:
			self.total = 0
		if self.normal_overtime is None:
			self.normal_overtime = 0
		super(Payroll, self).save(args, kwargs)

	def detail_url(self):
		"""
		show payroll details url on admin changelist page
		"""
		change_list_urls = reverse('admin:operational_payrolldetail_changelist')
		return format_html(
			"<a href='{0}?payroll__contract__employee__id__exact={1}'>Detail</a>",
			change_list_urls, self.contract.employee.id
		)
	detail_url.short_description = 'Other Salary Detail'
	detail_url.allow_tags = True

	def bank_account(self):
		return self.contract.employee.bank_account
	bank_account.short_description = 'Bank Account'

	@transition(field=state, source=State.DRAFT, target=State.FINAL,
			   custom=dict(verbose="Finalized Calculation",))
	def finalize(self):
		self.total = self.calculate_total()
		self.save(update='total')

	@transition(field=state, source=State.FINAL, target=State.DRAFT)
	def unfinalize(self):
		pass

	@transition(field=state, source=State.FINAL, target=State.PAID)
	def pay(self):
		pass

	def get_attendance(self):
		attendance = Attendance.objects.get(period=self.period, employee=self.contract.employee)
		return attendance

	def calculate_overtime(self, attendance, salary_per_day):
		rate = self.overtime
		ln = self.normal_overtime * attendance.ln
		lp = attendance.lp * Decimal(salary_per_day)
		lk = attendance.lk * Decimal(salary_per_day)
		l1 = attendance.l1 * rate * Decimal(1.50)
		l2 = attendance.l2 * rate * Decimal(2.00)
		l3 = attendance.l3 * rate * Decimal(3.00)
		l4 = attendance.l4 * rate * Decimal(4.00)
		return ln + lp + lk + l1 + l2 + l3 + l4
	calculate_overtime.short_description = 'Total Overtime'

	def calculate_decrease(self, attendance, salary_per_day):
		if attendance:
			total = (
				(attendance.alpha_day + attendance.sick_day + attendance.leave_day)
				* salary_per_day.quantize(Decimal("0.00"))
			)
		return total
	calculate_decrease.short_description = 'Decrease'

	def calculate_total(self):
		attendance = self.get_attendance()
		salary_per_day = self.base_salary_per_day
		total = self.base_salary + self.back_pay

		# adding other salary details
		other_salaries = self.payrolldetail_set.select_related('salary').all()
		for detail in other_salaries:
			detail.salary.name
			if detail.salary.calculate_condition == '+':
				total += detail.value
			else:
				total -= detail.value

		decrease = self.calculate_decrease(attendance, salary_per_day)
		overtime = self.calculate_overtime(attendance, salary_per_day.quantize(Decimal("0.00")))
		return (total + overtime - decrease).quantize(Decimal("0.00"))
	calculate_total.short_description = 'Total'


class PayrollDetail(models.Model):
	payroll = models.ForeignKey(Payroll, verbose_name='Payroll')
	salary = models.ForeignKey(SalaryName, verbose_name='Component')
	value = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name='Value')
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


class FinalPayroll(Payroll):
	objects = FinalPayrollManager()
	class Meta:
		proxy = True
		verbose_name = 'Finalized Payroll'
		verbose_name_plural = 'Finalized Payroll'


class FinalPayrollDetail(PayrollDetail):
	class Meta:
		proxy = True
		verbose_name = 'Finalized Payroll Detail'
		verbose_name_plural = 'Finalized Payroll Detail'


class CourseType(models.Model):
	name = models.CharField(verbose_name='Name', max_length=255)

	class Meta:
		verbose_name = 'Courses Type'
		verbose_name_plural = 'Courses Type'

	def __str__(self):
		return self.name


class Course(models.Model):
	name = models.CharField(verbose_name='Name', max_length=255)
	course_type = models.ForeignKey(CourseType, verbose_name='Course Type')

	class Meta:
		verbose_name = 'Course'
		verbose_name_plural = 'Courses'

	def __str__(self):
		return self.name


class TrainingSchedule(models.Model):
	date = models.DateField(verbose_name='Date')
	course = models.ForeignKey(Course, verbose_name='Courses')
	has_certificate = models.BooleanField(default=True, verbose_name='Certificate')
	presenter = models.CharField(verbose_name='Presenter', max_length=45)

	class Meta:
		verbose_name = 'Training Schedule'
		verbose_name_plural = 'Training Schedule'

	def __str__(self):
		return str(self.date)


class TrainingClass(models.Model):
	employee = models.ForeignKey(Employee, verbose_name='Employee')
	schedule = models.ForeignKey(TrainingSchedule, verbose_name='Schedule')

	class Meta:
		verbose_name = 'Training Class'
		verbose_name_plural = 'Training Classes'

	def __str__(self):
		return self.employee