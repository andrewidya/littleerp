from datetime import date, timedelta

from django.test import TestCase
from django.utils import timezone

from operational.models import PayrollPeriod
from operational.forms import PayrollPeriodForm


class PayrollPeriodFormTest(TestCase):
    def setUp(self):
        super(PayrollPeriodFormTest, self).setUp()
        self.payroll_period = PayrollPeriod.objects.create(
            date_create=timezone.now().date(),
            start_date=timezone.now().date(),
            end_date=(timezone.now() + timedelta(days=30)).date()
        )

    def test_payroll_period_model(self):
        obj = self.payroll_period
        self.assertEqual(obj.state, 'OPEN')
        self.assertEqual(obj.period, self.payroll_period.end_date.strftime('%Y-%m'))

    def test_payroll_period_close_state(self):
        obj = self.payroll_period
        obj.close()
        self.assertEqual(obj.state, 'CLOSE')

    def test_payroll_period_form(self):
        data = {
            'start_date': date(2017, 1, 1),
            'end_date': date(2017, 1, 30)
        }
        form = PayrollPeriodForm(data=data)
        self.assertTrue(form.is_valid())

    def test_payroll_period_form_in_past_end_date(self):
        data = {
            'start_date': date(2017, 1, 1),
            'end_date': date(2016, 12, 1)
        }
        form = PayrollPeriodForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('end_date', form.errors)
        self.assertEqual(form.errors['end_date'], [u'this field must be greater than Start Date'])
