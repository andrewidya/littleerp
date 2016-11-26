from django.db import models
from django.db.models import Q


class PaidPayrollManager(models.Manager):
    def get_queryset(self):
        return (super(PaidPayrollManager, self)
                .get_queryset()
                .select_related('period', 'staff', 'contract', 'contract__employee')
                .prefetch_related('payrolldetail_set')
                .filter(Q(state='PAID')))


class InvoiceManager(models.Manager):
    def get_queryset(self):
        return (super(InvoiceManager, self)
                .get_queryset()
                .prefetch_related('invoice_detail', 'invoicedetail_set')
                .select_related('sales_order').all())
