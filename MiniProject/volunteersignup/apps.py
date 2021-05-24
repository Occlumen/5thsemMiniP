from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class VolunteersignupConfig(AppConfig):
    name = 'volunteersignup'

    def ready(self):
        import volunteersignup.signals
