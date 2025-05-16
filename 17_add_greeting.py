import types
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"

    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        return (f"My name is {self.name}.")
    
person = Person("ALI")
print(person.say_name())
print(person.greet())