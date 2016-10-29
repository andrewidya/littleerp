from fsm_admin.mixins import FSMTransitionMixin

from django.contrib import admin

from finance.models import PaidPayroll, FinalPayrollPeriod, ProcessedPayroll
# Register your models here.

@admin.register(PaidPayroll)
class PaidPayrollAdmin(admin.ModelAdmin):
	fields = ('period', 'contract', 'base_salary')
	list_display = ('period', 'contract', 'base_salary', 'overtime', 'back_pay', 'staff', 'detail_url', 'state')
	list_filter = ('period__period',)
	readonly_fields = ('period', 'contract', 'base_salary')

	def has_add_permission(self, request):
		return False

	def get_actions(self, request):
		actions = super(PaidPayrollAdmin, self).get_actions(request)
		if 'delete_selected' in actions:
			del actions['delete_selected']
		return actions


class ProcessedPayrollInline(admin.TabularInline):
	model = ProcessedPayroll
	extra = 0
	fields = ('contract', 'staff', 'state')
	readonly_fields = ('contract', 'staff', 'state')
	max_num = 0
	can_delete = False


@admin.register(FinalPayrollPeriod)
class FinalPayrollPeriodAdmin(FSMTransitionMixin, admin.ModelAdmin):
	fields = ('period', ('start_date', 'end_date'), 'state')
	list_display = ('period', 'start_date', 'end_date', 'state')
	readonly_fields = ('period', 'start_date', 'end_date', 'state')
	inlines = [ProcessedPayrollInline]

	def has_add_permission(self, request):
		return False

	def has_delete_permission(self, request, obj=None):
		return False

