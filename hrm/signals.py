from datetime import datetime

from django.db.models import Sum
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from hrm.models import EvaluationDetail, LeaveTaken, AnnualLeave, LeaveType


@receiver(post_save, sender=EvaluationDetail)
def set_evaluation_ranking(sender, instance, created, **kwargs):
    instance.evaluation.evaluation_rate()
    instance.evaluation.save()


@receiver(post_save, sender=LeaveTaken)
def update_annual_leave(sender, instance, created, **kwargs):
	print("Updating")
	annual_leave, created = AnnualLeave.objects.get_or_create(
		employee=instance.employee,
		leave_type=instance.leave_type,
		year=instance.from_date.year,
		defaults={
			'year': int(instance.from_date.year),
			'day_allowed': 12
		}
	)

	current_leave_type_taken_day = LeaveTaken.objects.filter(
		employee=instance.employee,
		leave_type=instance.leave_type,
		from_date__year=instance.from_date.year,
		to_date__year=instance.to_date.year).aggregate(Sum('day')
	)
	annual_leave.remaining_day_allowed = annual_leave.day_allowed - current_leave_type_taken_day['day__sum']
	annual_leave.save()

@receiver(post_delete, sender=LeaveTaken)
def update_leave(sender, instance, **kwargs):
	print("Update Deletion")
	annual_leave, created = AnnualLeave.objects.get_or_create(
		employee=instance.employee,
		leave_type=instance.leave_type,
		year=instance.to_date.year
	)
	annual_leave.remaining_day_allowed += instance.day
	annual_leave.save()