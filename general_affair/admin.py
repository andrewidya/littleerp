from functools import update_wrapper

from datetime import datetime

from fsm_admin.mixins import FSMTransitionMixin

from django.conf.urls import url
from django.contrib import admin

from general_affair.models import (Supplier, SupplierBusinessType,
                                   ItemType, ItemCategory, Item, PurchaseOrder,
                                   OrderReceipt, ItemIssued, IDReleaseType,
                                   IDCard)
from reporting.response import PDFResponse


def get_model_info(obj):
    app_label = obj.model._meta.app_label
    try:
        return (app_label, obj.model._meta.model_name,)
    except AttributeError:
        return (app_label, obj.model._meta.module_name,)


def wrap(obj, view):
    def wrapper(*args, **kwargs):
        return obj.admin_site.admin_view(view, cacheable=True)(*args, **kwargs)
    return update_wrapper(wrapper, view)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone_number',
        'address',
        'business_type'
    )
    fieldsets = (
        ('General Info', {
            'fields': (
                'name',
                'address',
                'phone_number',
                'business_type',
            )
        }),
        ('Business Info', {
            'fields': (
                'owner',
                'tax_id_number',
                'owner_id_number',
                'siup_number',
                'tdp_number',
            )
        }),
        ('Partnership & Contract', {
            'fields': (
                'join_date',
                'start_date',
                'end_date',
                'description'
            )
        })
    )
    search_fields = ('name', )

    def get_urls(self):
        urls = super(SupplierAdmin, self).get_urls()
        info = get_model_info(self)
        admin_extra_url = [
            url(r'report/$', self.admin_site.admin_view(self.report), name='%s_%s_report' % info)
        ]

        return admin_extra_url + urls

    def report(self, request, *args, **kwargs):
        queryset = self.model._default_manager.get_queryset()
        template = 'general_affair/report/supplier.html'
        context = {
            'suppliers': queryset,
            'today': datetime.now()
        }
        return PDFResponse(request, template, context, filename='Supplier.pdf')


@admin.register(SupplierBusinessType)
class SupplierBusinessTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
        'item_type',
        'item_category'
    )
    list_filter = ('item_type__name', 'item_category__name')
    search_fields = ('code', 'name')


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(FSMTransitionMixin, admin.ModelAdmin):
    list_display = (
        'get_po_number',
        'item',
        'supplier',
        'quantity',
        'order_date',
        'state'
    )
    fields = (
        'number',
        'order_date',
        'item',
        'quantity',
        'supplier'
    )
    list_filter = ('item__name', )
    search_fields = ('number', 'item__name')


@admin.register(OrderReceipt)
class OrderReceiptAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'purchase_order',
        'quantity',
        'receipt_date'
    )
    search_fields = ('number', 'purchase_order__number')


@admin.register(ItemIssued)
class ItemIssuedAdmin(admin.ModelAdmin):
    list_display = (
        'item',
        'quantity',
        'date_issued',
        'recipient',
        'allocation'
    )


@admin.register(IDReleaseType)
class IDReleaseTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(IDCard)
class IDCardAdmin(admin.ModelAdmin):
    list_display = (
        'employee',
        'date_created',
        'date_expired',
        'status',
        'release_type'
    )
