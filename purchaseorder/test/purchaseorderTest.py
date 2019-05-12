import unittest

from mockito import mock, when, verify

from purchaseorder import Store
from purchaseorder.PurchaseOrder import PurchaseOrder


class PurchaseOrderTestMethods(unittest.TestCase):

    def setUp(self):
        self.store: Store= mock()

    def test_should_buy_remove_the_products_if_the_amount_is_enough(self):
        when(self.store).there_are_enough_products("milk", 25).thenReturn(True)

        purchase_order = PurchaseOrder("milk", 25)
        purchase_order.buy(self.store)

        verify(self.store, times=1).remove_products("milk", 25)

    def test_should_buy_not_remove_the_products_if_the_amount_is_not_enough(self):
        when(self.store).there_are_enough_products("milk", 25).thenReturn(False)

        purchase_order = PurchaseOrder("milk", 25)
        purchase_order.buy(self.store)

        verify(self.store, times=0).remove_products("milk", 25)


if __name__ == "__main__":
    unittest.main()
