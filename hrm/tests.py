import datetime
from decimal import Decimal

from django.conf import settings
from django.test import TestCase
from django.utils import timezone

from crm.models import Customer, SalesOrder, SalesOrderDetail, Service
from hrm.models import (Employee, EmployeeContract, OtherSalary,
                        SalaryCategory, SalaryName)


class MiniErp():
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
