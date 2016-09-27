from django.contrib import admin
from operational.models import VisitCustomer, VisitPointRateItem, VisitCustomerDetail
# Register your models here.

class VisitCustomerDetailInline(admin.TabularInline):
	model = VisitCustomerDetail
	extra = 1

@admin.register(VisitCustomer)
class VisitCustomerAdmin(admin.ModelAdmin):
	list_display = ('visit_date', 'sales_order_reference', 'get_customer_name', 'subject')
	fieldsets = (
		('Visit Information', {
			'fields': (('subject', 'sales_order_reference'), 'visit_date', 'employee')
		}),
	)
	raw_id_fields = ('sales_order_reference',)
	autocomplete_lookup_fields = {
		'fk': ['sales_order_reference'],
	}
	inlines = [VisitCustomerDetailInline]
	filter_horizontal = ('employee',)

@admin.register(VisitPointRateItem)
class VisitPointRateItemAdmin(admin.ModelAdmin):
	pass

