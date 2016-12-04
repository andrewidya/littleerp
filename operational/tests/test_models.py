from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from operational.models import (PayrollPeriod, Attendance)


class PayrollPeriodModelTest(TestCase):
    def setUp(self):
        super(PayrollPeriodModelTest, self).setUp()
        self.payroll_period = PayrollPeriod.objects.create(
            date_create=timezone.now().date(),
            start_date=timezone.now().date(),
            end_date=(timezone.now() + timedelta(days=30)).date()
        )

    def tearDown(self):
        self.payroll_period.delete()
        del self.payroll_period
        super(PayrollPeriodModelTest, self).tearDown()

    def test_payroll_period_creation(self):
        self.assertIsNotNone(self.payroll_period)
        self.assertEqual(PayrollPeriod.objects.count(), 1)

    def test_default_state(self):
        self.assertEqual(self.payroll_period.state, u'OPEN')

    def test_close_state(self):
        self.payroll_period.close()
        self.assertEqual(self.payroll_period.state, u'CLOSE')


class AttendanceModelTest(TestCase):
    fixtures = [
        'bank.json',
        'division.json',
        'job_title.json',
        'payroll_period.json'
    ]

    def setUp(self):
        from hrm.models import Employee
        from django.contrib.auth.models import User

        super(AttendanceModelTest, self).setUp()
        self.payroll_period = PayrollPeriod.objects.get(pk=1)
        self.employee = Employee.objects.get(pk=1)
        self.user = User.objects.get(pk=1)
        self.attendance = Attendance.objects.create(
            work_day=26,
            sick_day=0,
            alpha_day=0,
            leave_day=0,
            leave_left=12,
            ln=0,
            lp=0,
            lk=0,
            l1=0,
            l2=0,
            l3=0,
            l4=0,
            employee=self.employee,
            period=self.payroll_period,
            staff=self.user
        )
