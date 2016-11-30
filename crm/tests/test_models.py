from datetime import date, timedelta
from decimal import Decimal

from django.test import TestCase
from django.utils.timezone import now as today

from crm.models import (Customer, ItemCategory, SalesOrder, SalesOrderDetail,
                        Satisfication, SatisficationDetail,
                        SatisficationPointCategory, SatisficationPointRateItem,
                        Service, ServiceSalaryDetail, ServiceSalaryItem)


class CustomerModel(TestCase):
    fixtures = ['customer.json']

    def test_delete(self):
        self.assertEqual(Customer.objects.count(), 6)
        customer = Customer.objects.get(pk=1)
        customer.delete()
        self.assertEqual(Customer.objects.count(), 5)


class ServiceModel(TestCase):
    def setUp(self):
        self.service = Service.objects.create(name="Security")

    def _get_service_object(self):
        return self.service

    def test_service_object(self):
        service = self._get_service_object()
        self.assertEqual(Service.objects.count(), 1)
        self.assertIsNotNone(service)
        self.assertEqual(service.name, u'Security')

    def test_delete(self):
        service = self._get_service_object()
        service.delete()
        self.assertEqual(Service.objects.count(), 0)


class ItemCategoryModel(TestCase):
    def setUp(self):
        self.item_category = ItemCategory.objects.create(name="Pendapatan Utama")

    def _get_item_category_object(self):
        return self.item_category

    def test_item_category_object(self):
        item_category = self._get_item_category_object()
        self.assertEqual(ItemCategory.objects.count(), 1)
        self.assertIsNotNone(item_category)
        self.assertEqual(item_category.name, u'Pendapatan Utama')

    def test_delete(self):
        item_category = self._get_item_category_object()
        item_category.delete()
        self.assertEqual(ItemCategory.objects.count(), 0)


class ServiceSalaryItemModel(TestCase):
    fixtures = ['item_category.json']

    def setUp(self):
        self.service_salary_item = ServiceSalaryItem.objects.create(
            name="Tunjangan Kehadiran",
            category=ItemCategory.objects.get(pk=1)
        )

    def _get_service_salary_item_object(self):
        return self.service_salary_item

    def test_service_salary_item_object(self):
        service_salary_item = self._get_service_salary_item_object()
        self.assertEqual(ServiceSalaryItem.objects.count(), 1)
        self.assertIsNotNone(service_salary_item)

    def test_delete(self):
        service_salary_item = self._get_service_salary_item_object()
        service_salary_item.delete()
        self.assertEqual(ServiceSalaryItem.objects.count(), 0)


class SalesOrderModel(TestCase):
    fixtures = ['customer.json', 'service.json']

    def test_sales_order_creation(self):
        sales_order = SalesOrder.objects.create(
            number=1,
            date_create=today(),
            date_start=today(),
            date_end=(today() + timedelta(days=60)),
            customer=Customer.objects.get(pk=1),
            tax=Decimal(0.1),
            fee=Decimal(0.1),
            fee_calculate_condition='TOTAL'
        )
        self.assertEqual(SalesOrder.objects.count(), 1)
        self.assertIsNotNone(sales_order)
        self.assertEqual(sales_order.total_price(), Decimal(0.00))


class SalesOrderDetailModel(TestCase):
    fixtures = ['customer.json', 'service.json', 'sales_order.json']

    def test_sales_order_detail_creation(self):
        sales_order = SalesOrder.objects.get(pk=1)
        sales_order_detail = SalesOrderDetail.objects.create(
            sales_order=sales_order,
            service=Service.objects.get(pk=1),
            quantity=10,
            basic_salary=Decimal(1400000.00)
        )
        self.assertIsNotNone(sales_order_detail)
        self.assertEqual(SalesOrderDetail.objects.count(), 1)
        self.assertEqual(sales_order.total_price(), 14000000.00)

        another_sales_order_detail = SalesOrderDetail.objects.create(
            sales_order=sales_order,
            service=Service.objects.get(pk=2),
            quantity=20,
            basic_salary=Decimal(1500000.00)
        )
        self.assertIsNotNone(another_sales_order_detail)
        self.assertEqual(SalesOrderDetail.objects.count(), 2)
        self.assertEqual(sales_order.total_price(), 44000000.00)


class ServiceSalaryDetailModel(TestCase):
    fixtures = [
        'customer.json',
        'service.json',
        'item_category.json',
        'sales_order.json',
        'sales_order_detail.json',
        'service_salary_item.json',
    ]

    def setUp(self):
        self.sales_order = SalesOrder.objects.get(pk=1)

    def _get_sales_order(self):
        return self.sales_order

    def test_service_salary_detail_creation(self):
        sales_order = self._get_sales_order()
        service_salary_detail = ServiceSalaryDetail.objects.create(
            service_order_detail=SalesOrderDetail.objects.get(pk=1),
            service_salary_item=ServiceSalaryItem.objects.get(pk=1),
            price=Decimal(100000.00)
        )
        another_service_salary_detail = ServiceSalaryDetail.objects.create(
            service_order_detail=SalesOrderDetail.objects.get(pk=1),
            service_salary_item=ServiceSalaryItem.objects.get(pk=2),
            price=Decimal(200000.00)
        )
        self.assertEqual(ServiceSalaryDetail.objects.count(), 2)
        self.assertIsNotNone(service_salary_detail)
        self.assertIsNotNone(another_service_salary_detail)
        self.assertEqual(sales_order.total_price(), Decimal(17000000.00))


class SatisficationPointCategoryModel(TestCase):
    def setUp(self):
        self.satisfication_point_category = SatisficationPointCategory.objects.create(
            name="Kerapian",
            description="Penilaian tentang kerapian personel"
        )

    def test_adding_satisfication_point_category_model(self):       
        self.assertIsNotNone(self.satisfication_point_category)
        self.assertEqual(SatisficationPointCategory.objects.count(), 1)

    def test_delete(self):
        self.satisfication_point_category.delete()
        self.assertEqual(SatisficationPointCategory.objects.count(), 0)


class SatisficationPointRateItemModel(TestCase):
    fixtures = ['satisfication_point_category.json']

    def setUp(self):
        self.satisfication_point_rate_item = SatisficationPointRateItem.objects.create(
            category=SatisficationPointCategory.objects.get(pk=1),
            name="Seragam",
        )

    def test_adding_satisfication_point_rate_item(self):
        self.assertIsNotNone(self.satisfication_point_rate_item)
        self.assertEqual(SatisficationPointRateItem.objects.count(), 1)

    def test_delete(self):
        self.satisfication_point_rate_item.delete()
        self.assertEqual(SatisficationPointRateItem.objects.count(), 0)


class SatisficationModel(TestCase):
    fixtures = [
        'customer.json',
        'service.json',
        'sales_order.json',
        'satisfication_point_category.json',
        'satisfication_point_rate_item.json'
    ]

    def setUp(self):
        self.satisfication = Satisfication.objects.create(
            create_date=date(2016, 12, 1),
            name="Penilaian Personel",
            sales_order=SalesOrder.objects.get(pk=1),
        )

    def test_adding_satisfication(self):
        self.assertIsNotNone(self.satisfication)
        self.assertEqual(Satisfication.objects.count(), 1)

    def test_adding_satisfication_detail(self):
        satisfication_detail = SatisficationDetail.objects.create(
            satisfication=self.satisfication,
            point_rate_item=SatisficationPointRateItem.objects.get(pk=1),
            value=6
        )
        self.assertIsNotNone(satisfication_detail)
        self.assertEqual(SatisficationDetail.objects.count(), 1)

    def test_delete(self):
        self.satisfication.delete()
        self.assertEqual(Satisfication.objects.count(), 0)
