from django.db.models.signals import post_save
from django.dispatch import receiver
from operational.models import Payroll, PayrollDetail

@receiver(post_save, sender=Payroll)
def autopopulate_data(sender, instance, created, **kwargs):
	if created:
		# checking all salary item list on contract of payroll
		# instance
		salary_list = []
		for salary in instance.contract.other_salary.all():
			salary_list.append(salary)

		# creating object based on information got from contract
		for detail in salary_list:
			obj = PayrollDetail(payroll=instance, salary=detail.salary_name,
				               value=detail.value)
			obj.save()
