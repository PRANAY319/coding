class Product:
    tax_rate=50

    def __init__(self,name,product):
        self.name=name
        self.product=product
    def final_price(self):
        self.product=Product.tax_rate
