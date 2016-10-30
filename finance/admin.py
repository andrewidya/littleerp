from fsm_admin.mixins import FSMTransitionMixin

from django.contrib import admin

from finance.models import PaidPayroll, FinalPayrollPeriod, ProcessedPayroll, PayrollDetail


class PaidPayrollDetailInline(admin.TabularInline):
	model = PayrollDetail
	fields = ('salary', 'value', 'note')
	readonly_fields = ('salary', 'value', 'note')
	max_num = 0
	can_delete = 0

	def has_add_permission(self, request):
		return False

	def has_delete_permission(self, request, obj=None):
		return False

@admin.register(PaidPayroll)
class PaidPayrollAdmin(admin.ModelAdmin):
	fields = ('period', 'contract', 'overtime', 'back_pay', 'base_salary', 'total')
	list_display = ('period', 'contract', 'total', 'bank_account', 'state')
	list_filter = ('period__period',)
	readonly_fields = ('period', 'contract', 'overtime', 'back_pay', 'base_salary', 'total')

	change_form_template = 'admin/finance/paidpayroll/change_form.html'

	inlines = [PaidPayrollDetailInline]

	def has_add_permission(self, request):
		return False

	def has_delete_permission(self, request, obj=None):
		return False

	def get_actions(self, request):
		actions = super(PaidPayrollAdmin, self).get_actions(request)
		if 'delete_selected' in actions:
			del actions['delete_selected']
		return actions


class ProcessedPayrollInline(admin.TabularInline):
	model = ProcessedPayroll
	extra = 0
	fields = ('contract', 'total', 'state')
	readonly_fields = ('contract', 'total', 'state')
	max_num = 0
	can_delete = False

	def has_add_permission(self, request):
		return False

	def has_delete_permission(self, request, obj=None):
		return False


@admin.register(FinalPayrollPeriod)
class FinalPayrollPeriodAdmin(FSMTransitionMixin, admin.ModelAdmin):
	fields = ('period', ('start_date', 'end_date'), 'state')
	list_display = ('period', 'start_date', 'end_date', 'total', 'state')
	readonly_fields = ('period', 'start_date', 'end_date', 'state')
	inlines = [ProcessedPayrollInline]

	change_form_template = 'admin/finance/finalpayrollperiod/change_form.html'

	def has_add_permission(self, request):
		return False

	def has_delete_permission(self, request, obj=None):
		return False

	def get_actions(self, request):
		actions = super(FinalPayrollPeriodAdmin, self).get_actions(request)
		if 'delete_selected' in actions:
			del actions['delete_selected']
		return actions

