from django.contrib import admin
from mp_supply.models import SalesOrder, ItemCategory, ItemDetail, ItemCost
# Register your models here.

admin.site.register(SalesOrder)
admin.site.register(ItemCategory)
admin.site.register(ItemDetail)
