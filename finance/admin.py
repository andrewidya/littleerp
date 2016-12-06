from functools import update_wrapper

from fsm_admin.mixins import FSMTransitionMixin
from jet.admin import CompactInline

from django.contrib import admin
from django.template import Context

from reporting.admin import HTMLModelReportMixin
from reporting.utils import HTML2PDF
from finance.models import (Invoice, InvoiceDetail, InvoicedItemType,
                            InvoiceState, InvoiceTransaction, PaidPayroll)
from finance.options import get_financial_statement
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
        payroll_list = queryset.select_related('contract', 'contract__employee').prefetch_related('payrolldetail_set')
        container = []
        for payroll in payroll_list:
            payroll_item = {}
            payroll_item['payroll'] = payroll
            payroll_item['detail'] = {
                'potongan': [],
                'tunjangan': [],
                'lain': []
            }
            for detail in (payroll.payrolldetail_set.select_related('salary', 'salary__salary_category').all()
                           .order_by('salary__salary_category')):
                if detail.salary.salary_category.name == "Potongan":
                    payroll_item['detail']['potongan'].append(detail)
                elif detail.salary.salary_category.name == "Tunjangan":
                    payroll_item['detail']['tunjangan'].append(detail)
                elif detail.salary.salary_category.name == "Lain-lain":
                    payroll_item['detail']['lain'].append(detail)
            container.append(payroll_item)
        context = Context({'container': container})
        html_pdf = HTML2PDF(context, template_name='finance/report/payslip.html', output='payslip.pdf')
        return html_pdf.render(request)
    print_payslip.short_description = 'Print payslip for selected payroll'


class InvoiceDetailInline(CompactInline):
    model = InvoiceDetail
    extra = 0

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.state != InvoiceState.DRAFT:
            return ('invoiced_item', 'period', 'amount', 'notes')
        return super(InvoiceDetailInline, self).get_readonly_fields(request, obj=obj)

    def get_max_num(self, request, obj=None, **kwargs):
        if obj is not None and obj.state != InvoiceState.DRAFT:
            return 0
        return super(InvoiceDetailInline, self).get_max_num(request, obj=obj, **kwargs)

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.state != InvoiceState.DRAFT:
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
    )
    fsm_field = ['state', ]
    report_context_object_name = 'invoice'
    report_template = 'finance/report/invoice.html'
    change_form_template = "admin/finance/change_form.html"
    list_select_related = True
    inlines = [InvoiceDetailInline]

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.state != InvoiceState.DRAFT:
            return ('sales_order', 'invoice_number')
        return super(InvoiceAdmin, self).get_readonly_fields(request, obj=obj)

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.state != InvoiceState.DRAFT:
            return False
        return super(InvoiceAdmin, self).has_delete_permission(request, obj=obj)

    def get_context_data(self, obj):
        invoice_item = obj.invoicedetail_set.all()
        customer = obj.sales_order.customer
        context = super(InvoiceAdmin, self).get_context_data(obj)
        context['invoice_item'] = invoice_item
        context['customer'] = customer
        return context


@admin.register(InvoicedItemType)
class InvoiceItemTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(InvoiceTransaction)
class InvoiceTransactionAdmin(admin.ModelAdmin):
    change_list_template = 'admin/finance/change_list_finance_report.html'

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
        record = get_financial_statement()
        finance_list = [obj for obj in record]
        print(finance_list)
        context = Context({'finance_list': finance_list})
        html_pdf = HTML2PDF(context, template_name='finance/report/finance_statement.html', output='document.pdf')
        return html_pdf.render(request)
