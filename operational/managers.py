from django.db.models import Q, Manager


class ProcessingPayrollManager(Manager):
    def get_queryset(self):
        return super(ProcessingPayrollManager, self).get_queryset().select_related(
            'contract__employee', 'period').filter(Q(state='DRAFT') | Q(state='FINAL'))


class PayrollPeriodManager(Manager):
    def get_queryset(self):
        return super(PayrollPeriodManager, self).get_queryset().prefetch_related(
            'payroll_set', 'attendance_set')
