from django.dispatch import receiver
from django.db.models.signals import pre_save

from inventory.models import Tool


@receiver(pre_save, sender=Tool)
def tool_owner(sender, instance, **kwargs):
    """
    Esta función se ejecutará antes de guardar una instancia de la herramienta.
    Cambiará el estado a False si la herramienta tiene un propietario.
    """
    if instance.owner:
        instance.state = False
    else:
        instance.state = True
