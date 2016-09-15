from django.db import models
from django.utils.translation import ugettext as _
from crm.models import Customer

# Create your models here.

class SalesOrder(models.Model):
	so_number = models.CharField(verbose_name=_('Sales Order Number'), max_length=50)
	date = models.DateField()
	customer = models.ForeignKey(Customer, verbose_name=_('Work Location'))
	man_power_need = models.IntegerField(null=True, blank=True)

	class Meta:
		verbose_name = 'Sales Order'

	def __str__(self):
		return self.so_number

	def total_price(self):
		item_detail = self.itemcost_set.all().filter(sales_order=self)
		item_cost = 0
		for cost in item_detail:
			item_cost += cost.value
		return "IDR" + '{:20,.2f}'.format(self.man_power_need * item_cost)

	def customer_head_office(self):
		return self.customer.customer.name

class ItemCategory(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=50)
	description = models.TextField(blank=True)

	class Meta:
		verbose_name = 'Item Category'
		verbose_name_plural = 'Item Categories'

	def __str__(self):
		return self.name

class ItemDetail(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=50)
	category = models.ForeignKey(ItemCategory)
	description = models.TextField(blank=True)
	item_cost = models.ManyToManyField(SalesOrder, through='ItemCost')

	class Meta:
		verbose_name = 'Item Detail'

	def __str__(self):
		return self.name

class ItemCost(models.Model):
	item_detail = models.ForeignKey(ItemDetail)
	sales_order = models.ForeignKey(SalesOrder)
	value = models.DecimalField(max_digits=10, decimal_places=2)

	class Meta:
		verbose_name = 'Item Cost'
		verbose_name_plural = 'Item Costs'
