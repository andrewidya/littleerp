from django_fsm import FSMField, transition

from django.db import models
from django.utils.translation import ugettext as _

from hrm.models import Employee


class PurchaseOrderState(object):
    DRAFT = 'DRAFT'
    ONGOING = 'ONGOING'
    CLOSE = 'CLOSE'
    CANCEL = 'CANCEL'

    CHOICES = (
        (DRAFT, DRAFT),
        (ONGOING, ONGOING),
        (CLOSE, CLOSE),
        (CANCEL, CANCEL)
    )


class SupplierBusinessType(models.Model):
    name = models.CharField(verbose_name=_('Bussiness Type'), max_length=40)

    class Meta:
        verbose_name = 'Supplier Bussiness Type'
        verbose_name_plural = 'Supplier Bussiness Type'

    def __unicode__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(verbose_name=_('Supplier Name'), max_length=50)
    address = models.CharField(verbose_name=_('Address'), max_length=100, blank=True)
    phone_number = models.CharField(verbose_name=_('Phone Number'), max_length=15, null=True, blank=True)
    business_type = models.ForeignKey(SupplierBusinessType, verbose_name=_('Bussiness Type'))
    owner = models.CharField(verbose_name=_('Owner'), max_length=50, blank=True)
    tax_id_number = models.CharField(verbose_name=_('NPWP'), max_length=30, blank=True)
    owner_id_number = models.CharField(verbose_name=_('ID Number'), max_length=15, null=True, blank=True)
    siup_number = models.CharField(verbose_name=_('SIUP'), max_length=30, blank=True)
    tdp_number = models.CharField(verbose_name=_('TDP'), max_length=30, blank=True)
    join_date = models.DateField(verbose_name=_('Join Date'), null=True, blank=True)
    start_date = models.DateField(verbose_name=_('Start Date'), null=True, blank=True)
    end_date = models.DateField(verbose_name=_('End Date'), null=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __unicode__(self):
        return self.name


class ItemType(models.Model):
    code = models.CharField(verbose_name=_('Code'), max_length=40, unique=True)
    name = models.CharField(verbose_name=_('Name'), max_length=40)

    class Meta:
        verbose_name = 'Item Type'
        verbose_name_plural = 'Item Types'

    def __unicode__(self):
        return self.code + " " + self.name


class ItemCategory(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=40)

    class Meta:
        verbose_name = 'Item Category'
        verbose_name_plural = 'Item Categories'

    def __unicode__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(verbose_name=_('Item'), max_length=255)
    code = models.CharField(verbose_name=_('Code'), max_length=20, unique=True)
    buy_price = models.DecimalField(verbose_name=_('Buy Price'), max_digits=12, decimal_places=2)
    sell_price = models.DecimalField(verbose_name=_('Sell Price'), max_digits=12, decimal_places=2)
    description = models.TextField(blank=True)
    item_type = models.ForeignKey(ItemType)
    item_category = models.ForeignKey(ItemCategory)
    stock = models.PositiveIntegerField(verbose_name=_('Availability'), default=0)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Item Lists & Stocks'

    def __unicode__(self):
        return self.name


class PurchaseOrder(models.Model):
    number = models.PositiveIntegerField(verbose_name=_('PO Number'), unique=True)
    order_date = models.DateField(verbose_name=_('Order Date'))
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'))
    item = models.ForeignKey(Item)
    supplier = models.ForeignKey(Supplier)
    state = FSMField(default=PurchaseOrderState.DRAFT, choices=PurchaseOrderState.CHOICES)

    class Meta:
        verbose_name = 'Purchase Order'
        verbose_name_plural = 'Purchase Order'

    def __unicode__(self):
        return "PO # {0}".format(str(self.number))

    def get_po_number(self):
        return self.__unicode__()
    get_po_number.short_description = 'PO Number'

    @transition(field=state, source=PurchaseOrderState.DRAFT, target=PurchaseOrderState.ONGOING)
    def on_going(self):
        pass

    @transition(field=state, source=PurchaseOrderState.ONGOING, target=PurchaseOrderState.CLOSE)
    def close(self):
        pass

    @transition(field=state,
                source=[PurchaseOrderState.DRAFT, PurchaseOrderState.ONGOING],
                target=PurchaseOrderState.CANCEL)
    def cancel(self):
        pass


class OrderReceipt(models.Model):
    number = models.PositiveIntegerField(verbose_name=_('Receipt Number'), unique=True)
    purchase_order = models.ForeignKey(PurchaseOrder, verbose_name=_('Purchase Order'), on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'))
    receipt_date = models.DateField(verbose_name=_('Receipt Date'))

    class Meta:
        verbose_name = 'Receipt Order'
        verbose_name_plural = 'Order Receipt'

    def __unicode__(self):
        return str(self.number)


class ItemIssued(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'))
    date_issued = models.DateField(verbose_name=_('Date Issued'))
    recipient = models.CharField(verbose_name=_('Recipient'), max_length=255)
    allocation = models.CharField(verbose_name=_('Allocation'), max_length=255)

    class Meta:
        verbose_name = 'Item Issued'
        verbose_name_plural = 'Item Issued'

    def __unicode__(self):
        return str(self.item)


class IDReleaseType(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=50)

    class Meta:
        verbose_name = 'Release Type'
        verbose_name_plural = 'Release Types'

    def __unicode__(self):
        return str(self.name)


class IDCard(models.Model):
    employee = models.ForeignKey(Employee, verbose_name=_('Employee'))
    date_created = models.DateField(verbose_name=_('Date Created'))
    date_expired = models.DateField(verbose_name=_('Expired'))
    status = models.BooleanField(verbose_name=_('Is Active'), default=False)
    release_type = models.ForeignKey(IDReleaseType, verbose_name=_('Release Type'))

    class Meta:
        verbose_name = 'ID Card'
        verbose_name_plural = 'ID Cards'

    def __unicode__(self):
        return str(self.employee.get_full_name())
