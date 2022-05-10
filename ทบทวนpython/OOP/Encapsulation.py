class Animal():
    def eat(self):
        print("Eating Eating!")
    
class Cat(Animal):

    def setName(self, text):
        self.name = text
        print("Setting New Cat Name = ", self.name)

    def eat(self):
        print("Meoww !!", self.name)

cat1 = Cat()
cat1.__name = "Kitty"
cat1.eat()