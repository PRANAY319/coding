'''. Design a class Product that:
•	Maintains a base tax rate applicable to all products.
•	Each product has a name and base price.
•	Has a method to compute final price including tax.
•	Can change tax rate for all products using one method.
•	Includes a function to check whether a given price is valid or not (non-negative and realistic).
Demonstrate:
1.	Creating multiple products.
2.	Changing the tax rate.
3.	Showing updated prices and validity checks. '''
class Product:
    tax_rate=0.01
    def __init__(self,name,base_price):
        self.name = name
        self.base_price= base_price
    def final_price(self):
        self.base_price = self.base_price+(self.base_price * Product.tax_rate)
    @classmethod
    def change_tax_rate(cls,new_tax_rate):
        cls.tax_rate = new_tax_rate
    @staticmethod
    def check_valid_price(price):
        return price >0 or price < 10000


p1 = Product("pranay",1000)
p2 = Product("nivas",5000)
print(p1.base_price)
print(Product.check_valid_price(1000))
print(Product.change_tax_rate(new_tax_rate=20))
print(p1.final_price)





