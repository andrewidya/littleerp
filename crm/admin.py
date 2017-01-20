from django.contrib import admin
from django.contrib.admin.views import main
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.safestring import mark_safe

from crm.forms import SatisficationDetailForm
from crm.models import (Customer, ItemCategory, SalesOrder, SalesOrderDetail,
                        Satisfication, SatisficationDetail,
                        SatisficationPointCategory, SatisficationPointRateItem,
                        Service, ServiceSalaryDetail, ServiceSalaryItem)
from crm.widgets import AdminImageWidget


class CustomerAdmin(admin.ModelAdmin):
    list_filter = ('parent', 'join_date')
    list_display = (
        'logo_tag',
        'code',
        'name',
        'tax_id_number',
        'phone_number',
        'pic_name',
        'join_date',
        'parent',
    )
    list_display_links = ('logo_tag', 'code')
    fieldsets = (
        ('Customer Information', {
            'fields': (
                'logo',
                ('code', 'name'), ('address', 'city'),
                ('phone_number', 'tax_id_number'),
                'pic_name', 'parent', 'join_date'
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
        'contract',
        'tax',
        'fee',
        'fee_calculate_condition',
        'reference',
        'note'
    )
    list_display = (
        'number',
        'contract',
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
                         % (reverse('admin:app_list', kwargs={'app_label': 'crm'}), obj.number))
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
    list_filter = ('service_order_detail__sales_order__number',)
    search_fields = ['service_order_detail__sales_order__number', 'service_salary_item__name']


class SatisficationDetailInline(admin.TabularInline):
    model = SatisficationDetail
    fields = ('satisfication', 'point_rate_item', 'value')
    extra = 1
    form = SatisficationDetailForm


@admin.register(SatisficationPointCategory)
class SatisficationPointCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(SatisficationPointRateItem)
class SatisficationPointRateItemAdmin(admin.ModelAdmin):
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
