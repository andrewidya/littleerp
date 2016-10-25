from django_cron import CronJobBase, Schedule
from django.utils import timezone
from django.conf import settings
import datetime
from hrm.models import EmployeeContract


class EmployeeContractCronJob(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'hrm.employee_contract_cron_job'

    def do(self):
        print("Checking contract")
        print(timezone.now())
        print("===========================================================")
        warning = timezone.now() + datetime.timedelta(days=settings.MINIERP_SETTINGS['HRM']['recontract_warning'])
        contract_list = EmployeeContract.objects.all().filter(end_date__lte=warning.date())
        for contract in contract_list:
            contract.contract_status = contract.check_contract_status()
            contract.save(update_fields=['contract_status'])
        print("===========================================================")
        print("DONE")
        print("===========================================================")
