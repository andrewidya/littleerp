from django.contrib import admin
from mp_supply.models import SalesOrder, ItemCategory, ItemDetail, ItemCost
# Register your models here.

class ItemCostInline(admin.TabularInline):
	model = ItemCost

class ItemDetailInline(admin.TabularInline):
	model = ItemDetail
	fieldsets = (
		('Grade Information', {
			'fields': ('name', 'category'),
			'classes': ('collapse')
		}),
	)

class SalesOrderAdmin(admin.ModelAdmin):
	list_display = ('so_number', 'date', 'customer_head_office', 'customer', 'total_price')
	inlines = [ItemCostInline,]

class ItemCategoryAdmin(admin.ModelAdmin):
	inlines = [ItemDetailInline,]

class ItemDetailAdmin(admin.ModelAdmin):
	list_display = ('name', 'category')

class ItemCostAdmin(admin.ModelAdmin):
	list_display = ('sales_order', 'item_detail', 'value')

admin.site.register(SalesOrder, SalesOrderAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(ItemDetail, ItemDetailAdmin)
admin.site.register(ItemCost, ItemCostAdmin)
