from datetime import timedelta, date
from decimal import Decimal

from django.test import TestCase
from django.utils import timezone

from hrm.models import (Employee, EmployeeContract, OtherSalary, SalaryName, LeaveType, LeaveTaken,
                        AnnualLeave)


class EmployeeModelTest(TestCase):
    fixtures = ['bank.json', 'division.json', 'job_title.json', 'employee.json']

    def setUp(self):
        self.employee = Employee.objects.get(pk=1)

    def test_get_fullname(self):
        self.assertEqual(self.employee.get_full_name(), u'RIDWAN')


class EmployeeContractModelTest(TestCase):
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
        'salary_name.json'
    ]

    def setUp(self):
        from crm.models import SalesOrderDetail

        self.sales_order_detail = SalesOrderDetail.objects.get(pk=1)
        self.employee = Employee.objects.get(pk=1)
        self.contract = EmployeeContract.objects.create(
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=30),
            employee=self.employee,
            service_related=self.sales_order_detail,
            base_salary=Decimal(1500000.00)
        )
        super(EmployeeContractModelTest, self).setUp()

    def tearDown(self):
        del self.sales_order_detail
        del self.employee
        del self.contract
        super(EmployeeContractModelTest, self).tearDown()

    def test_contract_base_salary(self):
        contract = self.contract
        self.assertEqual(contract.get_basic_salary(), Decimal(1500000.00))

    def test_contract_total_salaries(self):
        salary_type = SalaryName.objects.get(pk=1)
        contract = self.contract
        other_salary = OtherSalary.objects.create(
            employee_contract=contract,
            salary_name=salary_type,
            value=Decimal(200000.00)
        )
        self.assertIsNotNone(other_salary)
        self.assertEqual(contract.get_contract_salary(), Decimal(1300000.00))

    def test_contract_active_state(self):
        contract = self.contract
        self.assertEqual(contract.check_contract_status(), u'ACTIVE')

    def test_contract_need_renewal_state(self):
        contract = self.contract
        end_date = timezone.now() + timedelta(days=3)
        contract.end_date = end_date
        contract.save(update_fields=['end_date'])
        self.assertEqual(contract.check_contract_status(), u'NEED RENEWAL')

    def test_contract_expired_state(self):
        contract = self.contract
        start_date = timezone.now() - timedelta(days=30)
        end_date = start_date + timedelta(days=20)
        contract.start_date = start_date
        contract.end_date = end_date
        contract.save(update_fields=['start_date', 'end_date'])
        self.assertEqual(contract.check_contract_status(), u'EXPIRED')


class LeaveTest(TestCase):
    fixtures = ['division.json', 'job_title.json', 'bank.json', 'employee.json']

    def setUp(self):
        super(LeaveTest, self).setUp()
        self.employee = Employee.objects.get(pk=1)
        self.leave_type = LeaveType.objects.create(name="Annual")

    def tearDown(self):
        del self.employee
        super(LeaveTest, self).tearDown()

    def test_leave_creation(self):
        leave_taken = LeaveTaken.objects.create(
            employee=self.employee,
            leave_type=self.leave_type,
            from_date=date(2016, 1, 1),
            to_date=date(2016, 1, 3),
        )
        self.assertEqual(leave_taken.day, 3)

    def test_annual_leave_automatic_creation(self):
        leave_taken = LeaveTaken.objects.create(
            employee=self.employee,
            leave_type=self.leave_type,
            from_date=date(2016, 1, 1),
            to_date=date(2016, 1, 3),
        )
        annual_leave = AnnualLeave.objects.get(
            employee=leave_taken.employee,
            leave_type=leave_taken.leave_type,
            year=leave_taken.from_date.year
        )
        self.assertEqual(annual_leave.day_allowed, 12)
        self.assertEqual(annual_leave.remaining_day_allowed, 9)

    def test_annual_leave_remaining_day_allowed_updating(self):
        leave_taken = LeaveTaken.objects.create(
            employee=self.employee,
            leave_type=self.leave_type,
            from_date=date(2016, 1, 1),
            to_date=date(2016, 1, 3),
        )
        annual_leave = AnnualLeave.objects.get(
            employee=leave_taken.employee,
            leave_type=leave_taken.leave_type,
            year=leave_taken.from_date.year
        )
        self.assertEqual(annual_leave.day_allowed, 12)
        self.assertEqual(annual_leave.remaining_day_allowed, 9)

        annual_leave.day_allowed = 5
        annual_leave.save(update_fields=['day_allowed', 'remaining_day_allowed'])

        self.assertEqual(annual_leave.day_allowed, 5)
        self.assertEqual(annual_leave.remaining_day_allowed, 2)

    def test_annual_leave_remaining_day_allowed_after_deletion(self):
        leave_taken = LeaveTaken.objects.create(
            employee=self.employee,
            leave_type=self.leave_type,
            from_date=date(2016, 1, 1),
            to_date=date(2016, 1, 3),
        )
        leave_taken.delete()
        annual_leave = AnnualLeave.objects.get(
            employee=leave_taken.employee,
            leave_type=leave_taken.leave_type,
            year=leave_taken.from_date.year
        )
        self.assertEqual(annual_leave.remaining_day_allowed, 12)
