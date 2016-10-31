from functools import partial

from fsm_admin.mixins import FSMTransitionMixin

from django.contrib import admin
from django.forms.models import modelformset_factory
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.db import IntegrityError

from operational.models import (VisitCustomer, VisitPointRateItem, VisitCustomerDetail, PayrollPeriod, Attendance,
	Payroll, PayrollDetail, State, FinalPayroll, FinalPayrollDetail, CourseType, Course, TrainingSchedule, TrainingClass)
from operational.forms import PayrollPeriodForm, PayrollForm


class VisitCustomerDetailInline(admin.TabularInline):
	model = VisitCustomerDetail
	extra = 1


@admin.register(VisitCustomer)
class VisitCustomerAdmin(admin.ModelAdmin):
	list_display = ('visit_date', 'sales_order_reference',
				   'get_customer_name', 'subject')
	fieldsets = (
		('Visit Information', {
			'fields': (
				('subject', 'sales_order_reference'), 'visit_date', 'employee'
			)
		}),
	)
	raw_id_fields = ('sales_order_reference',)
	autocomplete_lookup_fields = {
		'fk': ['sales_order_reference'],
	}
	inlines = [VisitCustomerDetailInline]
	filter_horizontal = ('employee',)


@admin.register(VisitPointRateItem)
class VisitPointRateItemAdmin(admin.ModelAdmin):
	pass


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
	fields = (
		('employee', 'period'),
		('work_day', 'sick_day'),
		('alpha_day', 'leave_day'),
		'leave_left',
	)
	list_display = ('period', 'employee', 'work_day', 'sick_day', 'alpha_day', 'leave_day', 'leave_left', 'staff')
	# raw_id_fields = ('employee', 'period')
	list_filter = ('period__period',)
	# autocomplete_lookup_fields = {
	#	'fk': ['employee', 'period'],
	# }
	list_editable = ('work_day', 'sick_day', 'alpha_day', 'leave_day', 'leave_left')

	def save_model(self, request, obj, form, change):
		if getattr(obj, 'staff', None) is None:
			obj.staff = request.user
		obj.save()
		super(AttendanceAdmin, self).save_model(request, obj, form, change)

	def get_readonly_fields(self, request, obj=None):
		if obj is not None and obj.period.state == State.CLOSE:
			self.list_editable = ''
			return ('work_day', 'sick_day', 'alpha_day', 'leave_day', 'leave_left', 'employee', 'period')
		return super(AttendanceAdmin, self).get_readonly_fields(request, obj=obj)

	def has_change_permission(self, request, obj=None):
		if obj is not None:
			if obj.period.state == State.CLOSE:
				return False
		return True

	def has_delete_permission(self, request, obj=None):
		if obj is not None:
			if obj.period.state == State.CLOSE:
				return False
		return True


@admin.register(Payroll)
class PayrollAdmin(FSMTransitionMixin, admin.ModelAdmin):
	fields = ('period', 'contract', 'base_salary')
	list_display = ('period', 'contract', 'base_salary', 'overtime', 'back_pay',
				   'calculate_total', 'staff', 'detail_url', 'state')
	list_editable = ['base_salary', 'overtime', 'back_pay']
	list_filter = ('period__period',)
	fsm_field = ['state',]
	# change_form_template = 'fsm_admin/change_form.html'
	actions = ['make_final']
	form = PayrollForm

	def save_model(self, request, obj, form, change):
		if getattr(obj, 'staff', None) is None:
			obj.staff = request.user
		obj.save()
		super(PayrollAdmin, self).save_model(request, obj, form, change)

	def get_queryset(self, request):
		#queryset = super(PayrollAdmin, self).get_queryset(request)
		queryset = Payroll.draft_manager.all()
		if request.user.is_superuser or request.user.has_perm('operational.audit_payroll'):
			return queryset
		return queryset.filter(staff=request.user)

	def get_changelist_formset(self, request, **kwargs):
		defaults = {
			"formfield_callback": partial(self.formfield_for_dbfield, request=request),
		}
		defaults.update(kwargs)
		return modelformset_factory(self.model, self.get_changelist_form(request),
								   extra=0, fields=self.list_editable, **defaults)
	def make_final(self, request, queryset):
		# queryset.update(state=State.FINAL)
		for obj in queryset:
			obj.total = obj.calculate_total()
			obj.state = State.FINAL
			obj.save()
	make_final.short_description = 'Mark selected payroll as final'

	def response_change(self, request, obj):
		super(PayrollAdmin, self).response_change(request, obj)
		changelist_url = reverse('admin:operational_payroll_changelist')
		return redirect(changelist_url)


@admin.register(PayrollDetail)
class PayrollDetailAdmin(admin.ModelAdmin):
	list_display = ('period', 'contract', 'employee',  'salary', 'value', 'note')
	list_filter = ('payroll__contract__employee',)
	list_editable = ['value', 'note']


class PayrollInline(admin.TabularInline):
	model = Payroll
	exclude = ('staff', 'state', 'total')
	form = PayrollForm

	def get_queryset(self, request):
		#queryset = super(PayrollAdmin, self).get_queryset(request)
		queryset = Payroll.draft_manager.all()
		if request.user.is_superuser:
			return queryset
		return queryset.filter(staff=request.user)

	def get_readonly_fields(self, request, obj=None):
		if obj is not None and obj.state == State.CLOSE:
			return ('contract', 'base_salary', 'overtime', 'back_pay')
		return super(PayrollInline, self).get_readonly_fields(request, obj=obj)

	def get_max_num(self, request, obj=None, **kwargs):
		if obj is not None and obj.state == State.CLOSE:
			return 0
		return super(PayrollInline, self).get_max_num(request, obj=obj)

	def has_delete_permission(self, request, obj=None):
		if obj is not None and obj.state == State.CLOSE:
			return False
		return True


class FinalPayrollDetailInline(admin.TabularInline):
	model = FinalPayrollDetail
	extra = 0
	readonly_fields = ('salary', 'value', 'note')
	max_num = 0
	can_delete = False


@admin.register(FinalPayroll)
class FinalPayrollAdmin(FSMTransitionMixin, admin.ModelAdmin):
	fieldsets = (
		('Payroll Information', {
			'fields': (
				('period', 'contract'), ('base_salary', 'overtime', 'back_pay')
			)
		}),
	)
	list_display = ('period', 'contract', 'total', 'bank_account', 'staff', 'state')
	list_filter = ('period__period',)
	readonly_fields = ('period', 'contract', 'base_salary', 'overtime', 'back_pay')
	inlines = [FinalPayrollDetailInline]
	actions = ['make_paid']
	change_form_template = 'admin/operational/finalpayroll/change_form.html'

	def get_queryset(self, request):
		queryset = super(FinalPayrollAdmin, self).get_queryset(request)
		if request.user.is_superuser or request.user.has_perm('operational.audit_payroll'):
			return queryset
		return queryset.filter(staff=request.user)

	def response_change(self, request, obj):
		super(FinalPayrollAdmin, self).response_change(request, obj)
		changelist_url = reverse('admin:operational_finalpayroll_changelist')
		return redirect(changelist_url)

	def has_add_permission(self, request):
		return False

	def has_delete_permission(self, request, obj=None):
		return False

	def get_actions(self, request):
		actions = super(FinalPayrollAdmin, self).get_actions(request)
		if 'delete_selected' in actions:
			del actions['delete_selected']
		return actions

	def make_paid(self, request, queryset):
		queryset.update(state=State.PAID)
	make_paid.short_description = 'Mark selected payroll item as paid'

class AttendanceInline(admin.TabularInline):
	model = Attendance
	fields = ('employee', ('work_day', 'sick_day'), ('alpha_day', 'leave_day'), 'leave_left', 'ln', 'lp', 'lk', 'l1',
			 'l2', 'l3', 'l4')
	# raw_id_fields = ('employee',)
	# autocomplete_lookup_fields = {
	#	'fk': ['employee']
	# }
	# classes = ('grp-collapse grp-closed',)

	def get_readonly_fields(self, request, obj=None):
		if obj is not None:
			if obj.state == State.CLOSE:
				return ('employee', 'work_day', 'sick_day', 'alpha_day', 'leave_day', 'leave_left', 'ln', 'lp', 'lk',
					   'l1', 'l2', 'l3', 'l4')
		return super(AttendanceInline, self).get_readonly_fields(request, obj=obj)

	def get_max_num(self, request, obj=None, **kwargs):
		if obj is not None:
			if obj.state ==State.CLOSE:
				return 0
		return super(AttendanceInline, self).get_max_num(request, obj=obj)

	def has_delete_permission(self, request, obj=None):
		if obj is not None:
			if obj.state == State.CLOSE:
				return False
		return True


@admin.register(PayrollPeriod)
class PayrollPeriodAdmin(admin.ModelAdmin):
	list_display = ('period', 'date_create', 'start_date', 'end_date', 'payroll_urls')
	fieldsets = (
		('Period Information', {
			'fields': (('start_date', 'end_date'),)
		}),
	)
	list_filter = ('period',)
	inlines = [AttendanceInline, PayrollInline]

	def save_formset(self, request, form, formset, change):
		instances = formset.save(commit=False)
		for obj in formset.deleted_objects:
			obj.delete()
		for instance in instances:
			if hasattr(instance, 'staff'):
				instance.staff = request.user
			instance.save()
		formset.save_m2m()

	def get_readonly_fields(self, request, obj=None):
		readonly_fields = super(PayrollPeriodAdmin, self).get_readonly_fields(request, obj=obj)
		if obj is not None:
			if obj.state == State.CLOSE:
				return ('start_date', 'end_date')
		return readonly_fields


@admin.register(CourseType)
class CourseTypeAdmin(admin.ModelAdmin):
	pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	pass


@admin.register(TrainingSchedule)
class TrainingScheduleAdmin(admin.ModelAdmin):
	pass


@admin.register(TrainingClass)
class TrainingClassAdmin(admin.ModelAdmin):
	pass