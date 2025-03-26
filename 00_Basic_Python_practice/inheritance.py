class Calculator:
    def div(self, a, b):
        return a / b
    
class SafeCalculator(Calculator):
    def div(self, a, b):
        if b == 0:
            return 0
        else:
            return a / b

if __name__ == "__main__":
    calc = SafeCalculator()
    # print(calc.div(10, 2))

''' animal ex '''

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating")

    def make_sound(self):
        print("animal makes sound")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name}: mung mung")

    def fetch(self):
        print(f"{self.name} brings the ball")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name}: ya-ong ")

    def scratch(self):
        print(f"{self.name} scratches")

if __name__ == "__main__":
    generic_animal = Animal("cherry", 10)
    generic_animal.eat()
    generic_animal.make_sound()

    my_dog = Dog("dogggg", 2)
    my_dog.make_sound()
    my_dog.fetch()