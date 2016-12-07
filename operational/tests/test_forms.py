from datetime import date, timedelta
from decimal import Decimal

from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from hrm.models import Employee, EmployeeContract
from operational.models import PayrollPeriod, PeriodState
from operational.forms import PayrollPeriodForm, PayrollCreationForm


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


class PayrollCreationFormTest(TestCase):
    fixtures = [
        'bank.json',
        'division.json',
        'job_title.json',
        'employee.json',
        'customer.json',
        'sales_order.json',
        'sales_order_detail.json',
        'service.json',
        'salary_category.json',
        'salary_name.json',
        'employee_contract.json',
        'payroll_period.json',
        'user.json'
    ]

    def setUp(self):
        super(PayrollCreationFormTest, self).setUp()
        self.employee = Employee.objects.get(pk=1)
        self.period = PayrollPeriod.objects.get(pk=1)
        self.staff = User.objects.get(pk=1)
        self.contract = EmployeeContract.objects.get(pk=1)

    def test_payroll_add_in_open_state(self):
        data = {
            'contract': self.contract.pk,
            'period': self.period.pk,
            'base_salary': Decimal(3100000.00),
            'staff': self.staff.pk
        }
        self.assertEqual(self.period.state, u'OPEN')
        form = PayrollCreationForm(data=data)
        self.asserFalse(form.is_valid())
