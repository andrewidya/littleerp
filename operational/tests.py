from datetime import date

from django.test import TestCase

from hrm.models import Employee
from operational.models import PayrollPeriod
from operational.forms import PayrollPeriodForm


class PayrollPeriodTest(TestCase):
    def get_payroll_period(self):
        obj = PayrollPeriod.objects.create(
            pk=1,
            date_create=date(2016, 11, 28),
            start_date=date(2016, 12, 1),
            end_date=date(2016, 12, 30)
        )
        obj.save()
        return obj

    def test_payroll_period_model(self):
        obj = self.get_payroll_period()
        self.assertEqual(obj.state, 'OPEN')
        self.assertEqual(obj.period, '2016-12')

    def test_payroll_period_close_state(self):
        obj = self.get_payroll_period()
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
