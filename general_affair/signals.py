from django_fsm.signals import post_transition as fsm_post_transition

from django.dispatch import receiver

from general_affair.models import PurchaseOrder

@receiver(fsm_post_transition, sender=PurchaseOrder)
def db_state_transition_update(sender, instance=None, target=None, **kwargs):
	if not isinstance(instance, sender):
		return
	instance.state = target
	instance.save(update_fields=['state'])