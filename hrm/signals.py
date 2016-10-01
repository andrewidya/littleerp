from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from hrm.models import Evaluation, EvaluationDetail

@receiver(post_save, sender=EvaluationDetail)
def set_evaluation_ranking(sender, instance, created, **kwargs):
	instance.evaluation.evaluation_rate()
	instance.evaluation.save()


