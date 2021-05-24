from homepage.models import VolunteerBasic
from django.db.models import signals
from django.dispatch import receiver


@receiver(signals.post_save, sender=VolunteerBasic)
def create_vb(sender, instance, created, **kwargs):
    if created:
        print("Volunteer created.")

