class Animal:
    def __init__(self, name):
        self._name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


dog = Dog("Fido")
cat = Cat("Whiskers")
print(dog.speak())
print(cat.speak())
