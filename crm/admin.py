from django.contrib import admin
from django.http import HttpResponseBadRequest
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf.urls import url
import django_excel as exel
from crm.models import Customer
from crm.forms import UploadFileForm
from data_importer.importers import XLSImporter
# Register your models here.

class CustomerImporter(XLSImporter):
	class Meta:
		model = Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = ('code', 'name', 'tax_id_number', 'phone_number', 'join_date', 'parent')
	fieldsets = (
		('Customer Information', {
			'fields': ('code', 'name', 'phone_number' ,'address', 'tax_id_number', 'join_date', 'parent')
		}),
	)

	def get_urls(self):
		urls = super(CustomerAdmin, self).get_urls()
		urlpatterns = [
			url(r'upload/$', self.admin_site.admin_view(self.upload))
		]
		return urlpatterns + urls

	def upload(self, request):
		if request.method == 'POST':
			form = UploadFileForm(request.POST, request.FILES)
			if form.is_valid():
				filehandle = self.request.FILES['file']
				excel.make_respone(filehandle.get_sheet(), 'xls')
			else:
				return HttpResponseBadRequest()
		else:
			form = UploadFileForm()
		return render_to_response('crm/admin/upload_view.html', {'form': form}, context_instance=RequestContext(request))