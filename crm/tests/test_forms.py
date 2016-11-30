from datetime import date

from django.test import TestCase

from crm.forms import SatisficationDetailForm
from crm.models import SatisficationPointRateItem, Satisfication, SalesOrder


class SatisficationDetailFormTest(TestCase):
    fixtures = [
        'customer.json',
        'service.json',
        'sales_order.json',
        'satisfication_point_category.json',
        'satisfication_point_rate_item.json'
    ]

    def setUp(self):
        self.satisfication = Satisfication.objects.create(
            create_date=date(2016, 12, 1),
            name="Penilaian Personel",
            sales_order=SalesOrder.objects.get(pk=1),
        )
        self.point_rate_item = SatisficationPointRateItem.objects.get(pk=1)

    def test_save_validation_below_two(self):
        data = {
            'satisfication': self.satisfication.pk,
            'point_rate_item': self.point_rate_item.pk,
            'value': 1
        }

        form = SatisficationDetailForm(data=data)
        self.assertFalse(form.is_valid())

    def test_save_validation_above_five(self):
        data = {
            'satisfication': self.satisfication.pk,
            'point_rate_item': self.point_rate_item.pk,
            'value': 6
        }
        form = SatisficationDetailForm(data=data)
        self.assertFalse(form.is_valid())

    def test_save_validation_with_right_value(self):
        data = {
            'satisfication': self.satisfication.pk,
            'point_rate_item': self.point_rate_item.pk,
            'value': 4
        }
        form = SatisficationDetailForm(data=data)
        self.assertTrue(form.is_valid())
