from django_fsm.signals import post_transition as fsm_post_transition

from django.db.models.signals import post_save
from django.dispatch import receiver

from operational.models import Payroll, PayrollDetail


@receiver(post_save, sender=Payroll)
def autopopulate_data(sender, instance, created, **kwargs):
    """Signal use to autopopulate data for payroll details.

    This signal autopopulate payroll detail data based on
    ``EmployeeContract`` object records associated with the sender,
    in this case ``Payroll`` object.
    """
    if created:
        # checking all salary item list on contract of payroll
        # instance
        salary_list = []
        for salary in instance.contract.other_salary.all():
            salary_list.append(salary)

        # creating object based on information got from contract
        for detail in salary_list:
            obj = PayrollDetail(payroll=instance, salary=detail.salary_name, value=detail.value)
            obj.save()


@receiver(fsm_post_transition, sender=Payroll)
def db_state_transition_update(sender, instance=None, target=None, **kwargs):
    """Signal use to update state of ``Payroll`` object.

    This signal has side effect of udpate ``Payroll.total`` attribute
    value by calling ``Payroll.calculate_total()`` method.
    """
    if not isinstance(instance, sender):
        return
    instance.total = instance.calculate_total()
    instance.state = target
    instance.save(update_fields=['state', 'total'])
