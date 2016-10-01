from django.apps import AppConfig

class HRMConfig(AppConfig):
	name = 'hrm'
	verbose_name = 'HRM Application'

	def ready(self):
		import hrm.signals