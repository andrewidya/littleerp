from django.contrib import admin
from payroll.models import Payroll, PayrollPeriod, PayrollIncreaseItem, PayrollDecreaseItem, PayrollIncreaseDetail, PayrollDecreaseDetail
# Register your models here.


class PayrollIncreaseDetailInline(admin.TabularInline):
	model = PayrollIncreaseDetail

class PayrollDecreaseDetailInline(admin.TabularInline):
	model = PayrollDecreaseDetail

@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
	list_display = ('period', 'employee', 'customer', 'total_increasing_item')

	inlines = [PayrollIncreaseDetailInline, PayrollDecreaseDetailInline]

@admin.register(PayrollPeriod)
class PayrollPeriodAdmin(admin.ModelAdmin):
	pass

@admin.register(PayrollIncreaseItem)
class PayrollIncreaseItemAdmin(admin.ModelAdmin):
	pass

@admin.register(PayrollDecreaseItem)
class PayrollDecreaseItemAdmin(admin.ModelAdmin):
	pass

@admin.register(PayrollIncreaseDetail)
class PayrollIncreaseDetailAdmin(admin.ModelAdmin):
	list_display = ('payroll', 'customer',  'employee', 'item', 'value')

@admin.register(PayrollDecreaseDetail)
class PayrollDecreaseDetailAdmin(admin.ModelAdmin):
	pass