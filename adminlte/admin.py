from django.contrib.admin.sites import AdminSite

# Register your models here.

class AdminLTE(AdminSite):
	site_header = 'COPS ADMINISTRATION'
	index_template = 'adminlte/index.html'

adminlte = AdminLTE(name='admin_lte')