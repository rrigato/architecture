# https://en.wikipedia.org/wiki/Dynamic_dispatch#Example_in_Python
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")


def speak(pet):
    # Dynamically dispatches the speak method
    # pet can either be an instance of Cat or Dog
    pet.speak()

cat = Cat()
speak(cat)
dog = Dog()
speak(dog)