from import_export.admin import ExportMixin, ImportMixin

from decimal import Decimal
from django import template
from django.utils.formats import number_format

from utils.utilities import Terbilang

register = template.Library()


@register.simple_tag(name='has_export_feature', takes_context=True)
def has_export_feature(context):
    obj = context['cl']
    issubclass(obj, ExportMixin)
    return True


@register.simple_tag(name='has_import_feature', takes_context=True)
def has_import_feature(value, context):
    issubclass(value, ImportMixin)
    return True


@register.filter(name='to_nominal')
def to_nominal(value):
    return Terbilang(value) + " Rupiah"


@register.simple_tag(name='total_salary')
def total_salary(value):
    queryset = value
    total = 0
    for i in queryset:
        total += i.total
    return number_format(total, force_grouping=True)


@register.simple_tag(name='total_employee')
def total_employee(value):
    return len(value)
