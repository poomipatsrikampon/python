from unicodedata import name


class Customer:
    name = ""
    last_name = ""
    age = 0
    def addCart(self):
        print("Added to Cart",self.name,self.last_name)

customer1 = Customer()
customer1.name = "Arm"
customer1.last_name = "Sr"
customer1.age = 26
customer1.addCart()

customer2 = Customer()
customer2.name = "Bee"
customer2.last_name = "V"
customer2.age = 24
customer2.addCart()