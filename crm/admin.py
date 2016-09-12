from django.contrib import admin
from crm.models import Customer, Branch
# Register your models here.

class BranchInline(admin.TabularInline):
	model = Branch

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('code', 'name', 'tax_id_number', 'phone_number', 'join_date')
	fieldsets = (
		('Customer Information', {
			'fields': ('code', 'name', 'phone_number' ,'address', 'tax_id_number', 'join_date')
		}),
	)

	inlines = [
		BranchInline
	]

class BranchAdmin(admin.ModelAdmin):
	list_display = ('customer', 'code', 'name', 'phone_number', 'city')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Branch, BranchAdmin)