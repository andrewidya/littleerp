from django.utils import timezone
import datetime
from hrm.models import EmployeeContract, Employee
from crm.models import Customer, SalesOrder, SalesOrderDetail, Service
# Create your tests here.

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
		employee = Employee(reg_number="EMP001", first_name="Andry",
						birth_place="Surabaya", birth_date=datetime.datetime(1988, 1, 25, 0, 0),
						date_of_hire=datetime.datetime(2016, 1, 1, 0, 0),
						marital_status='K/1')
		employee.save()
		return employee

	def create_customer(self):
		customer = Customer(code="CUS001", name="Django co",
						join_date=datetime.datetime(2015, 12, 15, 0, 0))
		customer.save()
		return customer

	def create_sales_order(self):
		sales_order = SalesOrder(number="SO001", date_create=timezone.now(),
							date_start=datetime.datetime(2016, 1, 1, 0, 0),
							date_end=datetime.datetime(2016, 12, 30, 0, 0),
							customer=self.customer, tax=0.00, fee=0.12,
							fee_calculate_condition='BASIC')
		sales_order.save()
		return sales_order

	def create_service(self):
		service = Service(name='Security')
		service.save()
		return service

	def create_sales_order_detail(self):
		sales_order_detail = SalesOrderDetail(sales_order=self.sales_order, service=self.service,
										quantity=10, basic_salary=1500000)
		sales_order_detail.save()
		return sales_order_detail

	def create_employee_contract(self):
		contract = EmployeeContract(start_date=datetime.datetime(2016, 9, 1, 0, 0),
									end_date=datetime.datetime(2016, 10, 30, 0, 0),
									employee=self.employee, service_related=self.sales_order_detail,
									basic_salary=1500000)
		contract.save()
		return contract