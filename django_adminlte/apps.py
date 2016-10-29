from django.apps import AppConfig


class DjangoAdminLTEConfig(AppConfig):
    name = 'django_adminlte'
    verbose_name = 'Django AdminLTE Theme'

    def ready(self):
        pass
