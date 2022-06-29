class Product:
    def __init__(self,name, price,amount,category=None,supplier=None ):
        self.name = name
        self.price = price
        self.amount = amount
        self.category = category
        self.supplier = supplier

class SaleProduct:
    def __init__(self, product_id, product_amount,total_price):
        self.product_id = product_id
        self.procut_amonut = product_amount
        self.total_price = total_price
