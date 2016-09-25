from django.contrib import admin
from crm.models import Customer, SalesOrder, SalesOrderDetail, ItemCategory, ServiceSalaryDetail, ServiceSalaryItem, Service, ServiceSalaryDetail
from crm import forms
from import_export.admin import ImportExportMixin, ImportMixin

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(ImportExportMixin, admin.ModelAdmin):
	list_filter = ('parent', 'join_date')
	list_display = ('code', 'name', 'tax_id_number', 'phone_number', 'join_date', 'parent')
	fieldsets = (
		('Customer Information', {
			'fields': ('code', 'name', 'phone_number' ,'address', 'city', 'tax_id_number', 'join_date', 'parent')
		}),
	)
	search_fields = ['parent__name', 'join_date', 'phone_number', 'city', 'code']
	change_list_template = "admin/change_list_filter_sidebar.html"

class SalesOrderDetailInline(admin.TabularInline):
	model = SalesOrderDetail
	fields = (('service', 'quantity', 'basic_salary'))

class ServiceSalaryDetailInline(admin.TabularInline):
	model = ServiceSalaryDetail

@admin.register(SalesOrder)
class SalesOrderAdmin(ImportExportMixin, admin.ModelAdmin):
	fields = ('number', ('date_create', 'date_start', 'date_end'), ('customer', 'reference'), 'tax', ('fee', 'fee_calculate_condition'), 'note')
	list_display = ('number', 'customer', 'date_start', 'date_end', 'tax', 'fee', 'service_demand_list', 'total_price', 'sales_order_detail_page')
	list_filter = ('number', 'customer')
	inlines = [SalesOrderDetailInline]
	search_fields = ['number', 'date_create', 'date_end', 'customer__name']

@admin.register(SalesOrderDetail)
class SalesOrderDetailAdmin(ImportExportMixin, admin.ModelAdmin):
	list_display = ('sales_order', 'get_service',  'quantity', 'basic_salary')
	list_filter = ('service', 'sales_order__number', 'sales_order__customer')
	search_fields = ['sales_order__number']
	inlines = [ServiceSalaryDetailInline]
	raw_id_fields = ('sales_order',)
	autocomplete_lookup_fields = {
		'fk': ['sales_order'],
	}
	change_list_template = "admin/change_list_filter_sidebar.html"

@admin.register(ItemCategory)
class ItemCategoryAdmin(ImportMixin, admin.ModelAdmin):
	pass

@admin.register(ServiceSalaryItem)
class ServiceSalaryItemAdmin(admin.ModelAdmin):
	list_display = ('name', 'category')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	pass

@admin.register(ServiceSalaryDetail)
class ServiceSalaryDetailAdmin(ImportExportMixin, admin.ModelAdmin):
	list_display = ('service_order_detail', 'service_salary_item', 'price')
	list_filter = ('service_order_detail__sales_order__number', 'price')
	search_fields = ['service_order_detail__sales_order__number']
	change_list_template = "admin/change_list_filter_sidebar.html"