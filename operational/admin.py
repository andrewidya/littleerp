from django.contrib import admin
from django.forms.models import modelformset_factory
from fsm_admin.mixins import FSMTransitionMixin
from functools import partial
from operational.models import VisitCustomer, VisitPointRateItem, \
	VisitCustomerDetail, PayrollPeriod, Attendance, Payroll, PayrollDetail, \
	State, PostProcessedPayroll
from operational.forms import PayrollPeriodForm
# Register your models here.

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
	fields = (('work_day', 'sick_day'), ('alpha_day', 'leave_day'),
		     'leave_left', ('employee', 'period'))
	list_display = ('period', 'employee', 'work_day', 'sick_day', 'alpha_day',
				   'leave_day', 'leave_left')
	raw_id_fields = ('employee', 'period')
	list_filter = ('period__period',)
	autocomplete_lookup_fields = {
		'fk': ['employee', 'period'],
	}
	list_editable = ('work_day', 'sick_day', 'alpha_day', 'leave_day',
				    'leave_left')

@admin.register(Payroll)
class PayrollAdmin(FSMTransitionMixin, admin.ModelAdmin):
	fields = ('period', 'contract', 'base_salary')
	list_display = ('period', 'contract', 'base_salary', 'overtime', 'back_pay',
				   'staff', 'detail_url', 'state')
	list_editable = ['base_salary', 'overtime', 'back_pay']
	list_filter = ('period__period',)
	fsm_field = ['state',]
	change_form_template = 'fsm_admin/change_form.html'
	actions = ['make_final']

	def save_model(self, request, obj, form, change):
		if getattr(obj, 'staff', None) is None:
			obj.staff = request.user
		obj.save()
		super(PayrollAdmin, self).save_model(request, obj, form, change)

	def get_queryset(self, request):
		#queryset = super(PayrollAdmin, self).get_queryset(request)
		queryset = Payroll.draft_manager.all()
		if request.user.is_superuser:
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
		queryset.update(state=State.FINAL)
	make_final.short_description = 'Mark selected payroll as final'

@admin.register(PayrollDetail)
class PayrollDetailAdmin(admin.ModelAdmin):
	list_display = ('period', 'contract', 'employee',  'salary', 'value',
				   'note')
	list_filter = ('payroll__contract__employee',)
	list_editable = ['value', 'note']

class PayrollInline(admin.TabularInline):
	model = Payroll
	exclude = ('staff',)
	classes = ('grp-collapse grp-closed',)
	raw_id_fields = ('contract',)
	autocomplete_lookup_fields = {
		'fk': ['contract']
	}

@admin.register(PostProcessedPayroll)
class PostProcessedPayrollAdmin(FSMTransitionMixin, admin.ModelAdmin):
	fields = ('period', 'contract', 'base_salary')
	list_display = ('period', 'contract', 'base_salary', 'overtime', 'back_pay',
				   'staff', 'detail_url', 'state')
	list_filter = ('period__period',)

class AttendanceInline(admin.TabularInline):
	model = Attendance
	fields = ('employee', ('work_day', 'sick_day'), ('alpha_day', 'leave_day'),
		     'leave_left')
	raw_id_fields = ('employee',)
	autocomplete_lookup_fields = {
		'fk': ['employee']
	}
	classes = ('grp-collapse grp-closed',)

@admin.register(PayrollPeriod)
class PayrollPeriodAdmin(admin.ModelAdmin):
	list_display = ('period', 'date_create', 'start_date', 'end_date',
				   'attendance_urls', 'payroll_urls')
	fieldsets = (
		('Period Information', {
			'fields': (('start_date', 'end_date'),)
		}),
	)
	list_filter = ('period',)
	inlines = [AttendanceInline, PayrollInline]
	form = PayrollPeriodForm

	def save_formset(self, request, form, formset, change):
		instances = formset.save(commit=False)
		for obj in formset.deleted_objects:
			obj.delete()
		for instance in instances:
			if hasattr(instance, 'staff'):
				instance.staff = request.user
			instance.save()
		formset.save_m2m()

