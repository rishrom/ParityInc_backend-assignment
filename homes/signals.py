from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import *

@receiver(post_save, sender=House)
@receiver(post_save, sender=Thermostat)
@receiver(post_save, sender=Room)
@receiver(post_save, sender=Light)
def record_model_instance_update(sender, instance, *args, **kwargs):
    pass

@receiver(post_delete, sender=House)
@receiver(post_delete, sender=Thermostat)
@receiver(post_delete, sender=Room)
@receiver(post_delete, sender=Light)
def record_model_instance_delete(sender, instance, *args, **kwargs):
    pass
