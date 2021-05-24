from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MembersignupConfig(AppConfig):
    name = 'membersignup'


    def ready(self):
        import membersignup.signals
