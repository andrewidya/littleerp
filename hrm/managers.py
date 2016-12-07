from django.db import models
from django.db.models import Q


class EmployeeContractManager(models.Manager):
    def get_queryset(self):
        return (super(EmployeeContractManager, self)
                .get_queryset()
                .select_related('employee', 'service_related')
                .filter(
                    Q(employee__is_active=True) &
                    (Q(contract_status='ACTIVE') |
                        Q(contract_status='NEED RENEWAL')))
                )


class DefaultEmployeeContractManager(models.Manager):
    def get_queryset(self):
        return super(DefaultEmployeeContractManager, self).get_queryset().select_related('employee', 'service_related')
