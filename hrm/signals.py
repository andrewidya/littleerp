from django.db.models import F
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from hrm.models import EvaluationDetail, LeaveTaken, AnnualLeave


@receiver(post_save, sender=EvaluationDetail)
def set_evaluation_ranking(sender, instance, created, **kwargs):
    instance.evaluation.evaluation_rate()
    instance.evaluation.save()


@receiver(post_save, sender=LeaveTaken)
def update_annual_leave(sender, instance, created, **kwargs):
    annual_leave, created = AnnualLeave.objects.get_or_create(
        employee=instance.employee,
        leave_type=instance.leave_type,
        year=instance.from_date.year,
        defaults={
            'year': int(instance.from_date.year),
            'day_allowed': 12
        }
    )

    if not created:
        annual_leave.update()


@receiver(post_delete, sender=LeaveTaken)
def update_leave(sender, instance, **kwargs):
    annual_leave, created = AnnualLeave.objects.get_or_create(
        employee=instance.employee,
        leave_type=instance.leave_type,
        year=instance.to_date.year
    )
    annual_leave.remaining_day_allowed = F('remaining_day_allowed') + instance.day
    annual_leave.save(update_fields=['remaining_day_allowed'])
