class MyClass:
    def __init__(self, name):
        self.name = name

    @classmethod
    def greet(cls):
        print(f"Hello from {cls.__name__}!")

    def say_hello(self):
        print(f"Hello, {self.name}!")

# Invoking class method without creating an instance
MyClass.greet()

# Creating an instance and invoking instance method
obj = MyClass("Alice")
obj.say_hello()
obj.greet()