import datetime
from decimal import Decimal

from django.conf import settings
from django.test import TestCase
from django.utils import timezone

from crm.models import Customer, SalesOrder, SalesOrderDetail, Service
from hrm.models import (Employee, EmployeeContract, OtherSalary,
                        SalaryCategory, SalaryName, LeaveType, AnnualLeave,
                        LeaveTaken, EvaluationPeriod, EvaluationItem, Evaluation,
                        EvaluationDetail)
from hrm.forms import (EmployeeContractForm, AnnualLeaveForm, LeaveTakenForm,
                       EvaluationDetailForm)


class MiniErp(object):
    def __init__(self):
        self.employee = self.create_employee()
        self.customer = self.create_customer()
        self.sales_order = self.create_sales_order()
        self.service = self.create_service()
        self.sales_order = self.create_sales_order()
        self.sales_order_detail = self.create_sales_order_detail()
        self.contract = self.create_employee_contract()

    def create_employee(self):
        employee = Employee(
            reg_number='S13238',
            first_name='Andry Widya',
            last_name='Putra UN',
            birth_place='Surabaya',
            birth_date=timezone.now(),
            phone_number='081554442968',
            gender='L',
            date_of_hire=timezone.now(),
            marital_status='K/1',
            is_active=True
        )
        employee.save()
        return employee

    def create_customer(self):
        customer = Customer(
            code="CUS001",
            name="Django co",
            join_date=datetime.datetime(2015, 12, 15, 0, 0)
        )
        customer.save()
        return customer

    def create_sales_order(self):
        sales_order = SalesOrder(
            number=1,
            date_create=timezone.now(),
            date_start=datetime.datetime(2016, 1, 1, 0, 0),
            date_end=datetime.datetime(2016, 12, 30, 0, 0),
            customer=self.customer, tax=0.00, fee=0.12,
            fee_calculate_condition='BASIC'
        )
        sales_order.save()
        return sales_order

    def create_service(self):
        service = Service(name='Security')
        service.save()
        return service

    def create_sales_order_detail(self):
        sales_order_detail = SalesOrderDetail(
            sales_order=self.sales_order,
            service=self.service,
            quantity=10,
            basic_salary=1500000
        )
        sales_order_detail.save()
        return sales_order_detail

    def create_employee_contract(self):
        contract = EmployeeContract(
            start_date=datetime.datetime(2016, 9, 1, 0, 0),
            end_date=datetime.datetime(2016, 10, 30, 0, 0),
            employee=self.employee,
            service_related=self.sales_order_detail,
            base_salary=1500000
        )
        contract.save()
        return contract


class EmployeeContractTest(TestCase):
    # fixtures = ['bank.json', 'division.json', 'job_title.json', 'employee.json']
    def setUp(self):
        super(EmployeeContractTest, self).setUp()
        self.minierp = MiniErp()

    def tearDown(self):
        super(EmployeeContractTest, self).tearDown()
        del self.minierp

    def test_active_status_in_contract(self):
        date = timezone.now() + datetime.timedelta(days=360)
        self.minierp.contract.end_date = date.date()
        self.minierp.contract.save(update_fields=['end_date'])
        self.assertEqual((self.minierp.contract.check_contract_status() == "ACTIVE"), True)

    def test_need_renewal_satus_in_contract(self):
        date = timezone.now() + datetime.timedelta(days=settings.MINIERP_SETTINGS['HRM']['recontract_warning'])
        self.minierp.contract.end_date = date.date()
        self.minierp.contract.save(update_fields=['end_date'])
        self.assertEqual((self.minierp.contract.check_contract_status() == "NEED RENEWAL"), True)

    def test_expired_status_in_contract(self):
        date = timezone.now() - datetime.timedelta(days=1)
        self.minierp.contract.end_date = date.date()
        self.minierp.contract.save(update_fields=['end_date'])
        self.assertEqual((self.minierp.contract.check_contract_status() == "EXPIRED"), True)

    def test_get_basic_salary_in_contract(self):
        self.assertEqual(self.minierp.contract.get_basic_salary(), Decimal(1500000.00))

    def test_adding_salaries_to_contract(self):
        salary_category = SalaryCategory.objects.create(name="Pendapatan Utama")
        decreasable_salary = SalaryName.objects.create(
            name="BPJS Kesehatan",
            salary_category=salary_category,
            calculate_condition="-"
        )
        increasable_salary = SalaryName.objects.create(
            name="Tunjangan Jabatan",
            salary_category=salary_category,
            calculate_condition="+"
        )
        decrease = OtherSalary.objects.create(
            employee_contract=self.minierp.contract,
            salary_name=decreasable_salary,
            value=Decimal(100000.00)
        )
        decrease.save()
        increase = OtherSalary.objects.create(
            employee_contract=self.minierp.contract,
            salary_name=increasable_salary,
            value=Decimal(200000.00)
        )
        increase.save()
        self.assertEqual(self.minierp.contract.get_contract_salary(), "IDR1,600,000.00")

    
    def test_employee_contract_form(self):
        employee = Employee.objects.get(pk=1)
        sales_order_detail = self.minierp.sales_order_detail
        data = {
            'start_date': datetime.date(2016, 11, 1),
            'end_date': datetime.date(2016, 11, 30),
            'employee': employee.pk,
            'service_related': sales_order_detail.pk,
            'base_salary': Decimal(3100000.00)
        }
        form = EmployeeContractForm(data=data)
        self.assertTrue(form.is_valid())


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
            from_date=datetime.date(2016, 1, 1),
            to_date=datetime.date(2016, 1, 3),
        )
        self.assertEqual(leave_taken.day, 3)

    def test_annual_leave_automatic_creation(self):
        leave_taken = LeaveTaken.objects.create(
            employee=self.employee,
            leave_type=self.leave_type,
            from_date=datetime.date(2016, 1, 1),
            to_date=datetime.date(2016, 1, 3),
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
            from_date=datetime.date(2016, 1, 1),
            to_date=datetime.date(2016, 1, 3),
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
            from_date=datetime.date(2016, 1, 1),
            to_date=datetime.date(2016, 1, 3),
        )
        leave_taken.delete()
        annual_leave = AnnualLeave.objects.get(
            employee=leave_taken.employee,
            leave_type=leave_taken.leave_type,
            year=leave_taken.from_date.year
        )

        self.assertEqual(annual_leave.remaining_day_allowed, 12)

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
            'from_date': datetime.date(2016, 1, 1),
            'to_date': datetime.date(2016, 1, 2)
        }
        form = LeaveTakenForm(data=data)
        self.assertTrue(form.is_valid())

    def test_leave_taken_form_different_year(self):
        data = {
            'employee': self.employee.pk,
            'leave_type': self.leave_type.pk,
            'from_date': datetime.date(2016, 1, 1),
            'to_date': datetime.date(2017, 1, 2)
        }
        form = LeaveTakenForm(data=data)
        self.assertFalse(form.is_valid())


class EvaluationTest(TestCase):
    fixtures = ['division.json', 'job_title.json', 'bank.json', 'employee.json']
    def setUp(self):
        self.eval_period = EvaluationPeriod.objects.create(
            evaluation_date=datetime.date(2016, 1, 1)
        )
        self.eval_item = EvaluationItem.objects.create(
            name="Kerapian"
        )
        self.eval = Evaluation.objects.create(
            date_create=datetime.date(2016, 1, 1),
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