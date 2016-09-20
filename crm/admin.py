from django.contrib import admin
from crm.models import Customer, SalesOrder

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = ('code', 'name', 'tax_id_number', 'phone_number', 'join_date', 'parent')
	fieldsets = (
		('Customer Information', {
			'fields': ('code', 'name', 'phone_number' ,'address', 'tax_id_number', 'join_date', 'parent')
		}),
	)

@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
	fields = ('number', ('date_create', 'date_start', 'date_end'), ('customer', 'reference'), 'tax', ('fee', 'fee_calculate_condition'), 'note')