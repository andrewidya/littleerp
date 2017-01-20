from django.core.urlresolvers import reverse
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _


class Customer(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, verbose_name=_('PIC'))
    code = models.CharField(verbose_name=_('Code'), max_length=10, unique=True)
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    phone_number = models.CharField(verbose_name=_('Phone Number'), max_length=15, null=True, blank=True)
    pic_name = models.CharField(verbose_name=_('Person In Charge'), max_length=15, null=True, blank=True)
    address = models.CharField(verbose_name=_('Address'), max_length=100, blank=True)
    city = models.CharField(verbose_name=_('City'), max_length=50, blank=True)
    field = models.CharField(verbose_name=_('Field'), max_length=20, blank=True)
    logo = models.ImageField(upload_to='crm/customer/logo/%Y/%m/%d', verbose_name='Logo', null=True, blank=True)
    tax_id_number = models.CharField(verbose_name=_('NPWP'), max_length=30, blank=True)
    join_date = models.DateField()

    class Meta:
        verbose_name = 'Customer List'
        verbose_name_plural = 'Customer Information'
        permissions = (
            ('view_only_customer', 'Can view only available customer'),
        )

    def __unicode__(self):
        return self.name

    @staticmethod
    def autocomplete_search_fields():
        return ('code', 'name')

    def logo_tag(self):
        if self.logo and hasattr(self.logo, 'url'):
            return mark_safe('<img src="{0}" width="35" height="35"'.format(self.logo.url))
        return mark_safe('<img src="/static/crm/img/unknown.jpg" width="35" height="35"')
    logo_tag.short_description = 'Logo'


class Service(models.Model):
    name = models.CharField(verbose_name=_('Service Provided'), max_length=255)

    class Meta:
        verbose_name = 'Service Provided'
        verbose_name = 'Service Provided List'

    def __unicode__(self):
        return self.name


class SalesOrder(models.Model):
    FEE_CONDITION_CHOICES = (
        ('BASIC', 'Basic Salary'),
        ('TOTAL', 'Grand Total')
    )
    number = models.IntegerField(verbose_name=_('SO Number'))
    date_create = models.DateField(verbose_name=_('Date Issued'))
    date_start = models.DateField(verbose_name=_('Contract Start Date'))
    date_end = models.DateField(verbose_name=_('Contract End Date'))
    customer = models.ForeignKey(Customer, verbose_name=_('Customer Name'))
    reference = models.CharField(verbose_name=_('Reference'), max_length=255, blank=True)
    contract = models.CharField(verbose_name=_('Contract Ref'), max_length=255, blank=True)
    note = models.TextField(blank=True)
    tax = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_('Tax'),
        help_text=_('Tax value must be decimal, ex: input 12\% / as 0.12')
    )
    fee = models.DecimalField(max_digits=12, decimal_places=3, verbose_name=_('Management Fee'))
    fee_calculate_condition = models.CharField(
        verbose_name=_('Fee Calculated Condition'),
        help_text=_('Set to basic if the fee will be calculated from basic salary, otherwise set to grand total'),
        max_length=5,
        choices=FEE_CONDITION_CHOICES
    )

    class Meta:
        verbose_name = 'Sales Order'
        verbose_name_plural = 'Sales Orders'

    def __unicode__(self):
        return 'SO # {0}'.format(self.number)

    def service_demand_list(self):
        sales_order_detail = self.salesorderdetail_set.all().filter(sales_order=self)
        service = ''
        for s in sales_order_detail:
            service += '<li>{0}</li>'.format(s.service.name.encode('utf-8'))
        return mark_safe('<ul>{0}</li>'.format(service))
    service_demand_list.allow_tags = True
    service_demand_list.short_description = 'Service Demand'

    def total_price(self):
        total = 0
        sales_order_detail = (self.salesorderdetail_set.all()
                              .filter(sales_order=self).prefetch_related('servicesalarydetail_set'))
        for service in sales_order_detail:
            service_price = 0
            salary = 0
            for service_salary in service.servicesalarydetail_set.all():
                salary += service_salary.price
            service_price = salary + service.basic_salary
            total += service_price * service.quantity
        return total
    total_price.short_description = 'Total Price'

    def sales_order_detail_page(self):
        return mark_safe('<a href="%ssalesorderdetail/?sales_order__number=%s">See Detail</a>'
                         % (reverse('admin:app_list', kwargs={'app_label': 'crm'}), self.number))
    sales_order_detail_page.short_description = 'Order Detail Link'

    @staticmethod
    def autocomplete_search_fields():
        return ('number', 'customer__name')


class SalesOrderDetail(models.Model):
    sales_order = models.ForeignKey(SalesOrder, verbose_name=_('Sales Order Number'))
    service = models.ForeignKey(Service, verbose_name=_('Service Demand'))
    quantity = models.SmallIntegerField(verbose_name=_('Unit Quantity'))
    basic_salary = models.DecimalField(
        verbose_name=_('Base Salary'),
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )
    other_salary_detail = models.ManyToManyField(
        'ServiceSalaryItem',
        through='ServiceSalaryDetail',
        related_name='other_salary_detail'
    )

    class Meta:
        verbose_name = 'Order Detail'
        verbose_name_plural = 'Order Details'

    def __unicode__(self):
        return "SO # " + str(self.sales_order.number) + " : " + self.service.name

    def get_service(self):
        return self.service.name
    get_service.short_description = 'Service'

    @staticmethod
    def autocomplete_search_fields():
        return ('sales_order__number', 'service__name')


class ItemCategory(models.Model):
    name = models.CharField(verbose_name=_('Item Category'), max_length=255)

    class Meta:
        verbose_name = 'Salary Category'
        verbose_name_plural = 'Salary Categories'

    def __unicode__(self):
        return self.name


class ServiceSalaryItem(models.Model):
    name = models.CharField(verbose_name=_('Price Item Component'), max_length=255)
    category = models.ForeignKey(
        ItemCategory,
        on_delete=models.CASCADE,
        verbose_name=_('Category'),
        related_name='service_price_item'
    )

    class Meta:
        verbose_name = 'Service Salary Item'
        verbose_name_plural = 'Service Salariy Items'

    def __unicode__(self):
        return self.name

    @staticmethod
    def autocomplete_search_fields():
        return ('name__icontains',)


class ServiceSalaryDetail(models.Model):
    service_order_detail = models.ForeignKey(
        SalesOrderDetail,
        verbose_name=_('Service Order Detail'),
        on_delete=models.CASCADE
    )
    service_salary_item = models.ForeignKey(
        ServiceSalaryItem,
        verbose_name=_('Salary Item'),
        on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = 'Detail Salary Per Service'
        verbose_name_plural = 'Detail Salary Per Service'
        unique_together = (('service_order_detail', 'service_salary_item'),)

    def __unicode__(self):
        return '{0}:{1}'.format(self.service_salary_item.name, self.service_order_detail.sales_order.number)


class SatisficationPointCategory(models.Model):
    name = models.CharField(
        verbose_name=_('Satisfication Point Category'),
        max_length=255
    )
    description = models.TextField(verbose_name=_('Description'), blank=True)

    class Meta:
        verbose_name = 'Satisfication Point Category'
        verbose_name_plural = 'Satisfication Point Categories'

    def __unicode__(self):
        return self.name


class SatisficationPointRateItem(models.Model):
    category = models.ForeignKey(SatisficationPointCategory, verbose_name=_('Point Category'))
    name = models.CharField(
        verbose_name=_('Satisfication Point Rate'),
        max_length=255,
        help_text=_('Point rate question for polling')
    )
    description = models.TextField(verbose_name=_('Description'), blank=True)

    class Meta:
        verbose_name = 'Satisfication Point Rate Item'
        verbose_name_plural = 'Satisfication Point Rate Item'

    def __unicode__(self):
        return self.name

    @staticmethod
    def autocomplete_search_fields():
        return ('name__icontains', 'category__name__icontains')


class Satisfication(models.Model):
    create_date = models.DateField(verbose_name=_('Date Created'))
    name = models.CharField(verbose_name=_('Subject'), max_length=255)
    sales_order = models.ForeignKey(SalesOrder, verbose_name=_('Related Sales Order'))
    respondent = models.CharField(verbose_name=_('Person Interviewed'), max_length=50, blank=True)

    class Meta:
        verbose_name = 'Satisfication'
        verbose_name_plural = 'Satisfication Interview'

    def __unicode__(self):
        return self.name


class SatisficationDetail(models.Model):
    satisfication = models.ForeignKey(Satisfication, verbose_name=_('Satisfication Subject'))
    point_rate_item = models.ForeignKey(SatisficationPointRateItem, verbose_name=_('Point Rate Item'))
    value = models.PositiveIntegerField(
        verbose_name=_('Point Value'),
        help_text=_('Value must be betwen 2 to 5')
    )

    class Meta:
        verbose_name = 'Satisfication Interview Detail'
        verbose_name_plural = 'Satisfication Interview Details'
        unique_together = ('satisfication', 'point_rate_item')

    def __unicode__(self):
        return '{0} {1}'.format(
            self.satisfication.sales_order.number,
            self.satisfication.sales_order.customer.name
        )

    def get_satisfication_point_rate_desc(self):
        return self.point_rate_item.description
