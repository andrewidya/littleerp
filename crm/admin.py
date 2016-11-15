from import_export.admin import ImportExportMixin, ImportMixin

from django.contrib import admin
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.admin.views import main

from crm import forms
from crm.forms import SatisficationDetailForm
from crm.widgets import AdminImageWidget
from crm.models import (
	Customer, SalesOrder, SalesOrderDetail, ItemCategory, ServiceSalaryDetail, ServiceSalaryItem,
	Service, ServiceSalaryDetail, Satisfication, SatisficationDetail, SatisficationPointRateItem,
	SatisficationPointCategory
)


class CustomerAdmin(ImportExportMixin, admin.ModelAdmin):
	list_filter = ('parent', 'join_date')
	list_display = (
		'logo_tag',
		'code',
		'name',
		'tax_id_number',
		'phone_number',
		'join_date',
		'parent',
	)
	fieldsets = (
		('Customer Information', {
			'fields': (
				'logo',
				('code', 'name'), ('address', 'city'),
				('phone_number', 'tax_id_number'),
				'parent', 'join_date'
			)
		}),
	)
	search_fields = [
		'parent__name',
		'join_date',
		'phone_number',
		'city',
		'code'
	]
	formfield_overrides = {
		models.ImageField: {'widget': AdminImageWidget}
	}

	def __init__(self, *args, **kwargs):
		super(CustomerAdmin, self).__init__(*args, **kwargs)
		main.EMPTY_CHANGELIST_VALUE = '-'

admin.site.register(Customer, CustomerAdmin)


class SalesOrderDetailInline(admin.TabularInline):
	model = SalesOrderDetail
	fields = (('service', 'quantity', 'basic_salary'))


class ServiceSalaryDetailInline(admin.TabularInline):
	model = ServiceSalaryDetail


@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
	fields = (
		'number',
		'date_create',
		('date_start', 'date_end'),
		'customer',
		'tax',
		'fee',
		'fee_calculate_condition',
		'reference',
		'note'
	)
	list_display = (
		'so_number',
		'customer',
		'date_start',
		'date_end',
		'tax',
		'fee',
		'service_demand_list',
		'total_price',
		'sales_order_detail_page'
	)
	list_filter = ('number',)
	search_fields = [
		'number',
		'date_create',
		'date_end',
		'customer__name'
	]
	inlines = [SalesOrderDetailInline]

	def get_queryset(self, request):
		return SalesOrder.objects.select_related('customer').all()

	def sales_order_detail_page(self, obj):
		return mark_safe('<a href="%ssalesorderdetail/?sales_order__number=%s">See Detail</a>'
			% (reverse('admin:app_list', kwargs={'app_label': 'crm'}), obj.number)
		)
	sales_order_detail_page.short_description = 'Order Detail Link'


@admin.register(SalesOrderDetail)
class SalesOrderDetailAdmin(admin.ModelAdmin):
	list_display = (
		'sales_order',
		'get_service',
		'quantity',
		'basic_salary'
	)
	list_filter = ('service', 'sales_order__number',)
	search_fields = ['sales_order__number', 'sales_order__customer__name']
	list_select_related = ('sales_order', 'service')
	inlines = [ServiceSalaryDetailInline]


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
	list_filter = ('service_order_detail__sales_order__number',)
	search_fields = ['service_order_detail__sales_order__number', 'service_salary_item__name']
	list_select_related = ('service_order_detail', 'service_salary_item')


class SatisficationDetailInline(admin.TabularInline):
	model = SatisficationDetail
	fields = ('satisfication', 'point_rate_item', 'value')
	extra = 1
	form = SatisficationDetailForm


@admin.register(SatisficationPointCategory)
class SatisficationPointCategoryAdmin(ImportMixin, admin.ModelAdmin):
	list_display = ('name', 'description')


@admin.register(SatisficationPointRateItem)
class SatisficationPointRateItemAdmin(ImportMixin, admin.ModelAdmin):
	list_display = ('name', 'category', 'description')


@admin.register(Satisfication)
class SatisficationAdmin(admin.ModelAdmin):
	list_display = (
		'create_date',
		'name',
		'sales_order',
		'respondent'
	)
	fields = (
		'name',
		('sales_order', 'create_date'),
		'respondent'
	)
	inlines = [SatisficationDetailInline]


@admin.register(SatisficationDetail)
class SatisficationDetailAdmin(admin.ModelAdmin):
	form = SatisficationDetailForm
	list_display = ('satisfication', 'point_rate_item', 'value')