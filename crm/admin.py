from django.contrib import admin
from crm.models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('code', 'name', 'tax_id_number', 'phone_number', 'join_date', 'parent')
	fieldsets = (
		('Customer Information', {
			'fields': ('code', 'name', 'phone_number' ,'address', 'tax_id_number', 'join_date', 'parent')
		}),
	)

admin.site.register(Customer, CustomerAdmin)