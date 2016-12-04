from datetime import date

from django.test import TestCase

from hrm.forms import EvaluationDetailForm, AnnualLeaveForm, LeaveTakenForm
from hrm.models import EvaluationPeriod, EvaluationItem, Evaluation, Employee, LeaveType


class EvaluationDetailFormTest(TestCase):
    fixtures = ['division.json', 'job_title.json', 'bank.json', 'employee.json']

    def setUp(self):
        self.eval_period = EvaluationPeriod.objects.create(
            evaluation_date=date(2016, 1, 1)
        )
        self.eval_item = EvaluationItem.objects.create(
            name="Kerapian"
        )
        self.eval = Evaluation.objects.create(
            date_create=date(2016, 1, 1),
            employee=Employee.objects.get(pk=1),
            eval_period=self.eval_period,
            evaluated_location="Surabaya"
        )

    def test_evaluation_detail_form(self):
        data = {
            'evaluation': self.eval.pk,
            'eval_item': self.eval_item.pk,
            'eval_value': 75
        }
        form = EvaluationDetailForm(data=data)
        self.assertTrue(form.is_valid())

    def test_evaluation_detail_with_ranking_value_gt_100(self):
        data = {
            'evaluation': self.eval.pk,
            'eval_item': self.eval_item.pk,
            'eval_value': 101
        }
        form = EvaluationDetailForm(data=data)
        self.assertFalse(form.is_valid())


class AnnualLeaveFormTest(TestCase):
    fixtures = ['division.json', 'job_title.json', 'bank.json', 'employee.json']

    def setUp(self):
        super(AnnualLeaveFormTest, self).setUp()
        self.employee = Employee.objects.get(pk=1)
        self.leave_type = LeaveType.objects.create(name="Annual")

    def tearDown(self):
        del self.employee
        super(AnnualLeaveFormTest, self).tearDown()

    def test_annual_leave_form(self):
        data = {
            'employee': self.employee.pk,
            'leave_type': self.leave_type.pk,
            'year': 2017,
            'day_allowed': 12
        }
        form = AnnualLeaveForm(data=data)
        self.assertTrue(form.is_valid())

    def test_leave_taken_form_within_same_year(self):
        data = {
            'employee': self.employee.pk,
            'leave_type': self.leave_type.pk,
            'from_date': date(2016, 1, 1),
            'to_date': date(2016, 1, 2)
        }
        form = LeaveTakenForm(data=data)
        self.assertTrue(form.is_valid())

    def test_leave_taken_form_different_year(self):
        data = {
            'employee': self.employee.pk,
            'leave_type': self.leave_type.pk,
            'from_date': date(2016, 1, 1),
            'to_date': date(2017, 1, 2)
        }
        form = LeaveTakenForm(data=data)
        self.assertFalse(form.is_valid())
