from purchaseorder import Store


class PurchaseOrder:
    def __init__(self, product_name:str, amount:int):
        self.product_name: str = product_name
        self.amount: int = amount

    def buy(self, store: Store):
        if store.there_are_enough_products(self.product_name, self.amount):
            store.remove_products(self.product_name, self.amount)