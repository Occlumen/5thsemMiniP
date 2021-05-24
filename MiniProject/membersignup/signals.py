from homepage.models import MemberBasic
from django.db.models import signals
from django.dispatch import receiver


@receiver(signals.post_save, sender=MemberBasic)
def create_mb(sender, instance, created, **kwargs):
    if created:
        print("Member created.")