from django.test import TestCase
from django.utils import timezone
from django.conf import settings
import datetime
from minierp.global_test_component import MiniErp

class EmployeeContractTest(TestCase):
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
