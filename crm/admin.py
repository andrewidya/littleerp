from django.contrib import admin
from crm.models import Customer, SalesOrder, SalesOrderDetail, ItemCategory, \
	ServiceSalaryDetail, ServiceSalaryItem, Service, ServiceSalaryDetail, \
	Satisfication, SatisficationDetail, SatisficationPointRateItem, \
	SatisficationPointCategory
from crm import forms
from import_export.admin import ImportExportMixin, ImportMixin
from django.utils.translation import ugettext as _
from django.contrib import messages
from crm.forms import SatisficationDetailForm

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(ImportExportMixin, admin.ModelAdmin):
	list_filter = ('parent', 'join_date')
	list_display = ('code', 'name', 'tax_id_number', 'phone_number',
				   'join_date', 'parent')
	fieldsets = (
		('Customer Information', {
			'fields': (
				('code', 'name'), ('address', 'city'),
				('phone_number', 'tax_id_number'),
				('parent', 'join_date')
			)
		}),
	)
	search_fields = ['parent__name', 'join_date', 'phone_number',
					'city', 'code']
	change_list_template = "admin/change_list_filter_sidebar.html"
	raw_id_fields = ('parent',)
	autocomplete_lookup_fields = {
		'fk': ['parent'],
	}

class SalesOrderDetailInline(admin.TabularInline):
	model = SalesOrderDetail
	fields = (('service', 'quantity', 'basic_salary'))

class ServiceSalaryDetailInline(admin.TabularInline):
	model = ServiceSalaryDetail
	raw_id_fields = ('service_salary_item',)
	autocomplete_lookup_fields = {
		'fk': ['service_salary_item'],
	}

@admin.register(SalesOrder)
class SalesOrderAdmin(ImportExportMixin, admin.ModelAdmin):
	fields = (
		'number',
		('date_create', 'date_start', 'date_end'),
		('customer', 'reference'), 'tax',
		('fee', 'fee_calculate_condition'),
		'note'
	)
	list_display = ('number', 'customer', 'date_start', 'date_end', 'tax',
				   'fee', 'service_demand_list', 'total_price',
				   'sales_order_detail_page')
	list_filter = ('number',)
	inlines = [SalesOrderDetailInline]
	search_fields = ['number', 'date_create', 'date_end', 'customer__name']

@admin.register(SalesOrderDetail)
class SalesOrderDetailAdmin(ImportExportMixin, admin.ModelAdmin):
	list_display = ('sales_order', 'get_service',  'quantity', 'basic_salary')
	list_filter = ('service', 'sales_order__number',)
	search_fields = ['sales_order__number', 'sales_order__customer__name']
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

class SatisficationDetailInline(admin.TabularInline):
	model = SatisficationDetail
	fields = ('satisfication', 'point_rate_item', 'value')
	form = SatisficationDetailForm
	extra = 1
	raw_id_fields = ('point_rate_item',)
	autocomplete_lookup_fields = {
		'fk': ['point_rate_item'],
	}

@admin.register(SatisficationPointCategory)
class SatisficationPointCategoryAdmin(ImportMixin, admin.ModelAdmin):
	list_display = ('name', 'description')

@admin.register(SatisficationPointRateItem)
class SatisficationPointRateItemAdmin(ImportMixin, admin.ModelAdmin):
	list_display = ('name', 'category', 'description')

@admin.register(Satisfication)
class SatisficationAdmin(admin.ModelAdmin):
	list_display = ('create_date', 'name', 'sales_order', 'respondent')
	inlines = [SatisficationDetailInline]
	fields = ('name', ('sales_order', 'create_date'), 'respondent')
	raw_id_fields = ('sales_order',)
	autocomplete_lookup_fields = {
		'fk': ['sales_order'],
	}

@admin.register(SatisficationDetail)
class SatisficationDetailAdmin(admin.ModelAdmin):
	form = SatisficationDetailForm
	list_display = ('satisfication', 'point_rate_item', 'value')
	raw_id_fields = ('point_rate_item',)
	autocomplete_lookup_fields = {
		'fk': ['point_rate_item'],
	}