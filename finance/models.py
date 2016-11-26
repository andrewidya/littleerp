from django_fsm import FSMField, transition

from django.db import models
from django.utils.translation import ugettext as _

from operational.models import Payroll, PayrollPeriod
from crm.models import SalesOrder
from finance.managers import PaidPayrollManager, InvoiceManager


class InvoiceState(object):
    '''
    Constants to represent the `state`s of the PublishableModel
    '''
    DRAFT = 'DRAFT'
    ONGOING = 'ONGOING'
    PAID = 'PAID'
    CANCEL = 'CANCEL'

    CHOICES = (
        (DRAFT, DRAFT),
        (ONGOING, ONGOING),
        (CANCEL, CANCEL),
        (PAID, PAID),
    )


class PaidPayroll(Payroll):
    objects = PaidPayrollManager()

    class Meta:
        proxy = True
        verbose_name = 'Payroll Payments History'
        verbose_name_plural = 'Payroll Payments History'


class Invoice(models.Model):
    sales_order = models.ForeignKey(SalesOrder, verbose_name=_('Sales Order'))
    invoice_number = models.PositiveIntegerField(verbose_name=_('Invoice Number'))
    state = FSMField(default=InvoiceState.DRAFT, choices=InvoiceState.CHOICES)
    date_create = models.DateField(auto_now_add=True, verbose_name=_('Date Created'))
    invoice_detail = models.ManyToManyField(
        'InvoicedItemType',
        through='InvoiceDetail',
        related_name='invoice_detail'
    )

    objects = InvoiceManager()

    class Meta:
        verbose_name = 'Invoice'

    def __unicode__(self):
        return str(("INV #" + str(self.invoice_number).zfill(4)))

    def formated_invoice_number(self):
        return str(("INV #" + str(self.invoice_number).zfill(4)))

    @transition(field=state, source=[InvoiceState.DRAFT, InvoiceState.ONGOING], target=InvoiceState.CANCEL)
    def cancel(self):
        pass

    @transition(field=state, source=InvoiceState.DRAFT, target=InvoiceState.ONGOING)
    def send(self):
        pass

    @transition(field=state, source=[InvoiceState.DRAFT, InvoiceState.ONGOING], target=InvoiceState.PAID)
    def paid(self):
        pass

    def calculate_total(self):
        total = 0
        for detail in self.invoicedetail_set.all():
            total += detail.amount
        return total


class InvoicedItemType(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Name'))

    class Meta:
        verbose_name = 'Invoiced Item Type'
        verbose_name_plural = 'Invoiced Item Type'

    def __unicode__(self):
        return self.name


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, verbose_name=_('Invoice'))
    invoiced_item = models.ForeignKey(InvoicedItemType, verbose_name=_('Invoiced Item'))
    period = models.ForeignKey(PayrollPeriod, limit_choices_to={'state': 'OPEN'}, verbose_name=_('Period'))
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_('Amount'))
    note = models.TextField(verbose_name='Notes', blank=True)

    class Meta:
        verbose_name = 'Invoice Detail'
        verbose_name_plural = 'Invoice Details'
        unique_together = ('invoiced_item', 'period')

    def __unicode__(self):
        return str(self.invoiced_item.name)


class TransactionType(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Name'))

    class Meta:
        verbose_name = 'Transaction Type'
        verbose_name_plural = 'Transaction Types'

    def __unicode__(self):
        return self.name


class InvoiceTransaction(models.Model):
    invoice = models.ForeignKey(Invoice, verbose_name=_('Invoice'), on_delete=models.PROTECT)
    transaction_type = models.ForeignKey(TransactionType, verbose_name=_('Transaction Type'), on_delete=models.PROTECT)
    date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_('Amount'))

    class Meta:
        verbose_name = 'Financial Transaction'
        verbose_name_plural = 'Financial Transactions'

    def __unicode__(self):
        return self.Invoice
