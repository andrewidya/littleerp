from django.contrib import admin
from crm.models import Customer, SalesOrder, SalesOrderDetail, ItemCategory, ServiceSalaryDetail, ServiceSalaryItem, Service, ServiceSalaryDetail
from crm import forms

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_filter = ('name', 'join_date')
	list_display = ('code', 'name', 'tax_id_number', 'phone_number', 'join_date', 'parent')
	fieldsets = (
		('Customer Information', {
			'fields': ('code', 'name', 'phone_number' ,'address', 'city', 'tax_id_number', 'join_date', 'parent')
		}),
	)
	form = forms.CustomerAddForm

class SalesOrderDetailInline(admin.TabularInline):
	model = SalesOrderDetail
	fields = (('service', 'quantity', 'basic_salary'))

class ServiceSalaryDetailInline(admin.TabularInline):
	model = ServiceSalaryDetail

@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
	fields = ('number', ('date_create', 'date_start', 'date_end'), ('customer', 'reference'), 'tax', ('fee', 'fee_calculate_condition'), 'note')
	list_display = ('number', 'customer', 'date_start', 'date_end', 'tax', 'fee')

	inlines = [SalesOrderDetailInline]

@admin.register(SalesOrderDetail)
class SalesOrderDetailAdmin(admin.ModelAdmin):
	list_display = ('sales_order', 'service', 'quantity', 'basic_salary')
	inlines = [ServiceSalaryDetailInline]

@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
	pass

@admin.register(ServiceSalaryItem)
class ServiceSalaryItemAdmin(admin.ModelAdmin):
	list_display = ('name', 'category')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	pass

@admin.register(ServiceSalaryDetail)
class ServiceSalaryDetailAdmin(admin.ModelAdmin):
	list_display = ('service_order_detail', 'service_salary_item', 'price')