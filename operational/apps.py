from django.apps import AppConfig


class OperationalConfig(AppConfig):
    name = 'operational'
    verbose_name = 'Operational Application'

    def ready(self):
        import operational.signals
