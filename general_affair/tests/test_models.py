from decimal import Decimal
from datetime import date

from django.test import TestCase
from django.db import IntegrityError

from general_affair.models import (ItemType, Item, ItemCategory,
                                   PurchaseOrder, Supplier, OrderReceipt,
                                   ItemIssued, IDReleaseType, IDCard)


class ItemTypeModelTest(TestCase):
    def setUp(self):
        self.item_type = ItemType.objects.create(
            code="A.1",
            name="Consumable"
        )
        self.item_type.save()

    def tearDown(self):
        del self.item_type

    def test_created_item_type(self):
        self.assertEqual(ItemType.objects.count(), 1)

    def test_unique_item_type_code(self):
        with self.assertRaises(IntegrityError):
            item_type = ItemType.objects.create(
                code="A.1",
                name="Material"
            )
            item_type.save()


class ItemModelTest(TestCase):
    fixtures = ['item_category.json', 'item_type.json']

    def setUp(self):
        self.item = Item.objects.create(
            name="ID Card",
            code="01.01",
            buy_price=Decimal(10000.00),
            sell_price=Decimal(12000.00),
            item_type=ItemType.objects.get(pk=1),
            item_category=ItemCategory.objects.get(pk=1)
        )
        self.item.save()

    def tearDown(self):
        del self.item

    def test_created_item(self):
        self.assertEqual(Item.objects.count(), 1)

    def test_unique_item(self):
        with self.assertRaises(IntegrityError):
            item = Item.objects.create(
                name="Seragam",
                code="01.01",
                buy_price=Decimal(70000.00),
                sell_price=Decimal(90000.00),
                item_type=ItemType.objects.get(pk=1),
                item_category=ItemCategory.objects.get(pk=1)
            )
            item.save()


class PurchaseOrderModelTest(TestCase):
    fixtures = [
        'item_category.json',
        'item_type.json',
        'item.json',
        'supplier_business_type.json',
        'supplier.json'
    ]

    def setUp(self):
        self.item = Item.objects.get(pk=1)
        self.supplier = Supplier.objects.get(pk=1)
        self.purchase_order = PurchaseOrder.objects.create(
            number=1,
            order_date=date(2016, 12, 8),
            quantity=10,
            item=self.item,
            supplier=self.supplier)

    def tearDown(self):
        del self.item
        del self.supplier
        del self.purchase_order

    def test_created_purchase_order(self):
        self.assertEqual(PurchaseOrder.objects.count(), 1)
        self.assertEqual(self.purchase_order.state, u'DRAFT')

    def test_on_going_purchase_order(self):
        self.purchase_order.on_going()
        self.assertEqual(self.purchase_order.state, u'ONGOING')

    def test_cancel_purchase_order(self):
        self.purchase_order.cancel()
        self.assertEqual(self.purchase_order.state, u'CANCEL')

    def test_close_purchase_order(self):
        self.purchase_order.on_going()
        self.purchase_order.close()
        self.assertEqual(self.purchase_order.state, u'CLOSE')


class OrderReceiptModelTest(TestCase):
    fixtures = [
        'item_category.json',
        'item_type.json',
        'item.json',
        'supplier_business_type.json',
        'supplier.json',
        'purchase_order.json'
    ]

    def setUp(self):
        self.purchase_order = PurchaseOrder.objects.get(pk=1)

    def tearDown(self):
        del self.purchase_order

    def test_created_order_receipt(self):
        order_receipt = OrderReceipt.objects.create(
            number=1,
            purchase_order=self.purchase_order,
            quantity=20,
            receipt_date=date(2016, 12, 8))
        order_receipt.save()
        self.assertEqual(OrderReceipt.objects.count(), 1)

    def test_item_stock(self):
        item = Item.objects.get(pk=1)
        self.assertEqual(item.stock, 0)

    def test_item_on_order_receipt(self):
        order_receipt = OrderReceipt.objects.create(
            number=1,
            purchase_order=self.purchase_order,
            quantity=20,
            receipt_date=date(2016, 12, 8))
        order_receipt.save()
        item = order_receipt.purchase_order.item
        self.assertEqual(item.stock, 20)
        order_receipt.delete()
        self.assertEqual(item.stock, 0)

    def test_item_stock_on_item_issued(self):
        order_receipt = OrderReceipt.objects.create(
            number=1,
            purchase_order=self.purchase_order,
            quantity=20,
            receipt_date=date(2016, 12, 8))
        order_receipt.save()
        item = order_receipt.purchase_order.item
        self.assertEqual(item.stock, 20)
        issued = ItemIssued.objects.create(
            item=item,
            quantity=5,
            date_issued=date(2016, 12, 8),
            recipient="Johan",
            allocation="Used"
        )
        issued.save()
        self.assertEqual(item.stock, 15)
        issued.delete()
        self.assertEqual(item.stock, 20)


class IDCardReleaseTest(TestCase):
    fixtures = [
        'bank.json',
        'division.json',
        'job_title.json',
        'employee.json'
    ]

    def setUp(self):
        from hrm.models import Employee

        self.id_release_type = IDReleaseType.objects.create(
            name="First Printing"
        )
        self.employee = Employee.objects.get(pk=1)

    def tearDown(self):
        del self.id_release_type
        del self.employee

    def test_created_id_card(self):
        id_card = IDCard.objects.create(
            employee=self.employee,
            date_created=date(2016, 12, 9),
            date_expired=date(2017, 12, 9),
            release_type=self.id_release_type
        )
        id_card.save()
        self.assertEqual(IDCard.objects.count(), 1)
