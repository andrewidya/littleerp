from decimal import Decimal
import datetime

from django.test import TestCase
from django.utils import timezone
from crm.models import (SalesOrder, Customer, Service, SalesOrderDetail, ItemCategory,
                        ServiceSalaryItem, ServiceSalaryDetail)


class SalesOrderTest(TestCase):
    fixtures = ['customer.json', 'service.json']

    def setUp(self):
        super(SalesOrderTest, self).setUp()
        self.customer = Customer.objects.get(pk=1)
        self.service = Service.objects.get(pk=1)
        self.today = timezone.now()
        self.sales_order = SalesOrder.objects.create(
            number=1,
            date_create=self.today,
            date_start=self.today,
            date_end=(self.today + datetime.timedelta(days=60)),
            customer=self.customer,
            tax=Decimal(0.1),
            fee=Decimal(0.1),
            fee_calculate_condition='TOTAL'
        )
        self.item_ategory = ItemCategory.objects.create(name="Pendapatan Utama")
        self.service_salary_item = ServiceSalaryItem.objects.create(
            name="Tunjangan Lembur",
            category=self.item_ategory
        )
        self.sales_order_detail = SalesOrderDetail.objects.create(
            sales_order=self.sales_order,
            service=self.service,
            quantity=10,
            basic_salary=Decimal(1400000)
        )
        self.service_salary_detail = ServiceSalaryDetail.objects.create(
            service_order_detail=self.sales_order_detail,
            service_salary_item=self.service_salary_item,
            price=Decimal(100000)
        )

    def test_sales_order_total_price(self):
        self.assertEqual((self.sales_order.total_price() == Decimal(15000000)), True)

    def test_adding_service_salary_item(self):
        salary = ServiceSalaryItem.objects.create(
            name="Tunjangan Jabatan",
            category=self.item_ategory
        )
        service_salary_detail = ServiceSalaryDetail.objects.create(
            service_order_detail=self.sales_order_detail,
            service_salary_item=salary,
            price=Decimal(100000)
        )
        service_salary_detail.save()
        self.assertEqual((self.sales_order.total_price() == Decimal(16000000)), True)
