from decimal import Decimal

from functools import update_wrapper

from fsm_admin.mixins import FSMTransitionMixin
from jet.admin import CompactInline

import django
from django.contrib import admin
from django.contrib.admin.options import IS_POPUP_VAR
from django.template.response import TemplateResponse

from reporting.admin import HTMLModelReportMixin
from reporting.response import PDFResponse
from finance.models import (Invoice, InvoiceDetail, InvoicedItemType,
                            InvoiceState, InvoiceTransaction, PaidPayroll,
                            TransactionType)
from finance.options import get_financial_statement
from finance.forms import FinanceStatementPeriodForm
from operational.models import PayrollDetail


class PaidPayrollDetailInline(admin.TabularInline):
    model = PayrollDetail
    fields = ('salary', 'value', 'note')
    readonly_fields = ('salary', 'value', 'note')
    max_num = 0
    can_delete = 0

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(PaidPayroll)
class PaidPayrollAdmin(admin.ModelAdmin):
    fields = (
        'period',
        'contract',
        'overtime',
        'back_pay',
        'base_salary',
        'total'
    )
    list_display = (
        'period',
        'contract',
        'total',
        'bank_account',
        'state'
    )
    readonly_fields = (
        'period',
        'contract',
        'overtime',
        'back_pay',
        'base_salary',
        'total'
    )
    list_filter = ('period__period',)
    change_form_template = 'admin/finance/paidpayroll/change_form.html'
    actions = ['print_payslip']
    inlines = [PaidPayrollDetailInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(PaidPayrollAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def print_payslip(self, request, queryset):
        """Print payslip action.

        Admin action to generate payslip in pdf format

        Parameters
        ----------
            request : ``HttpRequest``
                      Django request object
            queryset : queryset

        Return
        ------
            ``HttpResponse``
                      PDF data formated objects
        """
        payroll_list = queryset.select_related(
            'contract',
            'contract__employee'
        ).prefetch_related('payrolldetail_set')
        container = []
        for payroll in payroll_list:
            payroll_item = {}
            payroll_item['payroll'] = payroll
            payroll_item['detail'] = {
                'potongan': [],
                'tunjangan': [],
                'lain': []
            } 
            payroll_item['period'] = payroll.period.end_date
            data = payroll.payrolldetail_set.select_related(
                'salary',
                'salary__salary_category'
            ).all().order_by('salary__salary_category')
            for detail in data:
                if detail.salary.calculate_condition == "-":
                    payroll_item['detail']['potongan'].append(detail)
                elif "tunjangan" in detail.salary.salary_category.name.lower():
                    payroll_item['detail']['tunjangan'].append(detail)
                elif detail.salary.salary_category.name == "Lain-lain":
                    payroll_item['detail']['lain'].append(detail)
            container.append(payroll_item)
        context = {'container': container}

        template = 'finance/report/payslip.html'
        return PDFResponse(request, template, context, filename='payslip.pdf')
    print_payslip.short_description = 'Print payslip for selected payroll'


class InvoiceDetailInline(CompactInline):
    model = InvoiceDetail
    extra = 0

    def get_readonly_fields(self, request, obj=None):
        if obj:
            if obj.state != InvoiceState.DRAFT:
                return ('invoiced_item', 'period', 'amount', 'note')
        return super(InvoiceDetailInline, self).get_readonly_fields(request, obj=obj)

    def get_max_num(self, request, obj=None, **kwargs):
        if obj:
            if obj.state != InvoiceState.DRAFT:
                return 0
        return super(InvoiceDetailInline, self).get_max_num(request, obj=obj, **kwargs)

    def has_delete_permission(self, request, obj=None):
        if obj:
            if obj.state != InvoiceState.DRAFT:
                return False
        return super(InvoiceDetailInline, self).has_delete_permission(request, obj=obj)


@admin.register(Invoice)
class InvoiceAdmin(FSMTransitionMixin, HTMLModelReportMixin, admin.ModelAdmin):
    list_display = (
        'sales_order',
        'formated_invoice_number',
        'date_create',
        'state'
    )
    fieldsets = (
        ('General Information', {
            'fields': ('invoice_number', 'sales_order')
        }),
        ('Tax Information', {
            'fields': ('pph21', 'fee', 'ppn')
        })
    )
    report_context_object_name = 'invoice'
    report_template = 'finance/report/invoice.html'
    change_form_template = "admin/finance/change_form_fsm.html"
    list_select_related = True
    inlines = [InvoiceDetailInline]

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.state != InvoiceState.DRAFT:
            return ('sales_order', 'invoice_number', 'pph21', 'fee', 'ppn')
        return super(InvoiceAdmin, self).get_readonly_fields(request, obj=obj)

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.state != InvoiceState.DRAFT:
            return False
        return super(InvoiceAdmin, self).has_delete_permission(request, obj=obj)

    def get_fieldsets(self, request, obj=None):
        if not obj:
            fieldsets = (
                ('General Information', {
                    'fields': ('invoice_number', 'sales_order')
                }),
            )
            return fieldsets
        return super(InvoiceAdmin, self).get_fieldsets(request, obj)

    def get_inline_instances(self, request, obj=None):
        if obj is None:
            return []
        return super(InvoiceAdmin, self).get_inline_instances(request, obj)

    def response_add(self, request, obj, post_url_continue=None):
        if '_addanother' not in request.POST and IS_POPUP_VAR not in request.POST:
            request.POST['_continue'] = 1
        return super(InvoiceAdmin, self).response_add(request, obj, post_url_continue)

    def get_context_data(self, obj):
        invoice_item = obj.invoicedetail_set.all()
        total_invoice_detail = 0
        if invoice_item:
            for item in invoice_item:
                total_invoice_detail += item.amount
        pph21 = obj.pph21 * total_invoice_detail
        ppn = obj.ppn * total_invoice_detail
        fee = obj.fee * total_invoice_detail
        customer = obj.sales_order.customer
        context = super(InvoiceAdmin, self).get_context_data(obj)
        context['invoice_item'] = invoice_item
        context['customer'] = customer
        context['pph21'] = pph21.quantize(Decimal("0.00"))
        context['ppn'] = ppn.quantize(Decimal("0.00"))
        context['fee'] = fee.quantize(Decimal("0.00"))
        context['total'] = (fee + ppn + pph21 + total_invoice_detail).quantize(Decimal("0.00"))
        return context


@admin.register(InvoicedItemType)
class InvoiceItemTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(TransactionType)
class TransactionTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(InvoiceTransaction)
class InvoiceTransactionAdmin(admin.ModelAdmin):
    list_display = (
        'invoice',
        'transaction_type',
        'date',
        'amount'
    )
    # change_list_template = 'admin/finance/change_list_finance_report.html'
    report_intermediate_template = 'finance/finance_report_generation.html'

    def get_urls(self):
        """
        Get default django admin urls then add custom url for report link
        """
        from django.conf.urls import url

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view, cacheable=True)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        info = self.model._meta.app_label, self.model._meta.model_name

        urls = super(InvoiceTransactionAdmin, self).get_urls()
        finance_statement_url = [
            url(r'^generate_finance_statement/$',
                wrap(self.generate_finance_statement),
                name='%s_%s_generate_finance_statement' % info),
        ]
        return finance_statement_url + urls

    def generate_finance_statement(self, request):
        form = FinanceStatementPeriodForm(request.POST or None)

        if form.is_valid():
            record = get_financial_statement()
            finance_list = [obj for obj in record]
            context = {'finance_list': finance_list}
            template = 'finance/report/finance_statement.html'
            return PDFResponse(request, template, context, filename="finance_statement.pdf")

        context = {}

        if django.VERSION >= (1, 8, 0):
            context.update(self.admin_site.each_context(request))
        elif django.VERSION >= (1, 7, 0):
            context.update(self.admin_site.each_context())

        context['form'] = form
        context['opts'] = self.model._meta
        request.current_app = self.admin_site.name
        return TemplateResponse(request, [self.report_intermediate_template],
                                context)
