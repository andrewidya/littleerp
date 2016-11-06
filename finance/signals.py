from django_fsm.signals import post_transition as fsm_post_transition

from django.db.models.signals import post_save
from django.dispatch import receiver

from finance.models import Invoice


@receiver(fsm_post_transition, sender=Invoice)
def db_state_transition_update(sender, instance=None, target=None, **kwargs):
	if not isinstance(instance, sender):
		return

	instance.state = target
	instance.save(update_fields=['state'])