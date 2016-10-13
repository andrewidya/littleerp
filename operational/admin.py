from django.contrib import admin
from operational.models import VisitCustomer, VisitPointRateItem, \
	VisitCustomerDetail, PayrollPeriod, Attendance, Payroll, PayrollDetail
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

@admin.register(PayrollPeriod)
class PayrollPeriodAdmin(admin.ModelAdmin):
	list_display = ('period', 'date_create', 'start_date', 'end_date')
	fields = (('start_date', 'end_date'),)
	list_filter = ('period',)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
	fields = (('work_day', 'sick_day'), ('alpha_day', 'leave_day'),
		     'leave_left', ('employee', 'period'))
	list_display = ('period', 'employee', 'work_day', 'sick_day', 'alpha_day',
				   'leave_day', 'leave_left')
	raw_id_fields = ('employee', 'period')
	autocomplete_lookup_fields = {
		'fk': ['employee', 'period'],
	}

@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
	fields = ('period', 'contract', 'base_salary')
	list_display = ('period', 'contract', 'base_salary', 'overtime', 'back_pay',
				   'staff', 'detail_url')
	list_editable = ['base_salary', 'overtime', 'back_pay']

	def save_model(self, request, obj, form, change):
		if getattr(obj, 'staff', None) is None:
			obj.staff = request.user
		obj.save()

@admin.register(PayrollDetail)
class PayrollDetailAdmin(admin.ModelAdmin):
	list_display = ('period', 'contract', 'employee',  'salary', 'value',
				   'note')
	list_filter = ('payroll__contract__employee',)
	list_editable = ['value', 'note']