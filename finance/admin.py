from django.contrib import admin
from finance.models import PaidPayroll
# Register your models here.

@admin.register(PaidPayroll)
class PaidPayrollAdmin(admin.ModelAdmin):
	fields = ('period', 'contract', 'base_salary')
	list_display = ('period', 'contract', 'base_salary', 'overtime', 'back_pay',
				   'staff', 'detail_url', 'state')
	list_filter = ('period__period',)
	readonly_fields = ('period', 'contract', 'base_salary')

	def has_add_permission(self, request):
		return False

	def get_actions(self, request):
		actions = super(PaidPayrollAdmin, self).get_actions(request)
		if 'delete_selected' in actions:
			del actions['delete_selected']
		return actions
