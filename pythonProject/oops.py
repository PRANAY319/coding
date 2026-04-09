''' Create a class Animal with make_sound() and derived classes Dog, Cat, Cow that
override it.
Demonstrate polymorphism by iterating over a list of different animal objects and calling
make_sound()'''

'''class Animal:
    def make_sound(self):
        print("animal")
class Dog(Animal):
    def make_sound(self):
        print("Barking")
class  cat(Animal):
    def make_sound(self):
        print("MOAM")'''

'''class Car:
    def start(self):
        print("Car is starting")


class Computer:
    def start(self):
        print("Computer is booting")


class WashingMachine:
    def start(self):
        print("Washing Machine is running")


# Function that works with any object having a start() method
def operate(device):
    device.start()



# Passing different objects
c = Car()
pc = Computer()
wm = WashingMachine()
device = [Car,Computer,WashingMachine]
for i in device:
    print(Car.start)


operate(c)
operate(pc)
operate(wm)'''

'''class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Overload == operator
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # For clean printing
    def __str__(self):
        return f"Vector({self.x}, {self.y})"


# Creating objects
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = Vector(6, 8)

# Using + operator
result = v1 + v2

print("v1 + v2 =", result)

# Using == operator
print("v1 + v2 == v3 ?", result == v3)
'''




