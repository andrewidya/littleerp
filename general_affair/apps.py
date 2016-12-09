from django.apps import AppConfig


class GeneralAffairConfig(AppConfig):
    name = 'general_affair'
    verbose_name = 'General Affair'

    def ready(self):
        import general_affair.signals
