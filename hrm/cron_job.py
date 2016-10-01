from django_cron import CronJobBase, Schedule
from django.utils import timezone
from django.db.models import Q
import datetime
from hrm.models import EmployeeContract

class EmployeeContractCronJob(CronJobBase):
	RUN_EVERY_MINS = 1

	schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
	code = 'hrm.employee_contract_cron_job'

	def do(self):
		print("Checking contract")
		print(timezone.now())
		print(timezone.now() + datetime.timedelta(days=1))
		today = timezone.now()
		warning = timezone.now() + datetime.timedelta(days=10)
		contract_list = EmployeeContract.objects.all().filter(end_date__lte=warning.date())
		for contract in contract_list:
			if contract.end_date < today.date():
				contract.contract_status = "EXPIRED"
			if contract.end_date >= today.date() <= warning.date():
				contract.contract_status = "NEED RENEWAL"
			print(contract.contract_status)
			contract.save(update_fields=['contract_status'])

