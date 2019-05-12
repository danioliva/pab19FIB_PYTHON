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

    def test_should_buy_the_amount_is_enough_for_the_first_time_but_not_fir_the_second_one(self):
        when(self.store).there_are_enough_products("milk", 25).thenReturn(True)
        when(self.store).there_are_enough_prodcuts("milk", 30).thenReturn(False)

        purchase_order_yes = PurchaseOrder("milk", 25)
        purchase_order_no = PurchaseOrder("milk", 30)

        purchase_order_yes.buy(self.store)
        purchase_order_no.buy(self.store)

        verify(self.store, times=1).remove_products("milk",25)
        verify(self.store, times=0).remove_products("milk", 30)



if __name__ == "__main__":
    unittest.main()
