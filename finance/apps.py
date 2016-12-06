from django.apps import AppConfig


class FinanceConfig(AppConfig):
    name = 'finance'
    verbose_name = 'Financial Application'

    def ready(self):
        import finance.signals
