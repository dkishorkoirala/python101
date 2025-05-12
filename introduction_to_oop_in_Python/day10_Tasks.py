print(".................................................................................................................")

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display(self):
        print(f"The name of student is {self.name}, age is {self.age} and grade is {self.grade}")
    
student1 = Student("Kishor", 25, 10)
student1.display()

print(".................................................................................................................")

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def display(self):
        print(f"The title of book is {self.title}, author is {self.author} and pric is {self.price}.")

    def update_price(self, new_price):
        self.price = new_price
        print(f"The updated price of the book '{self.title}' is now {self.price}.")


book1 = Book("AI for Beginners", "OpenAI", 599)
book1.display()
book1.update_price(499)
book1.display()

print(".................................................................................................................")

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def display_info(self):
        super().display_info()
        print(f"Seats: {self.seats}")

class Bike(Vehicle):
    def __init__(self, brand, model, cc):
        super().__init__(brand, model)
        self.cc = cc

    def display_info(self):
        super().display_info()
        print(f"Engine: {self.cc}cc")

car1 = Car("Toyota", "Camry", 5)
bike1 = Bike("Yamaha", "R15", 150)

car1.display_info()
print("----------------------------------------------------------------")
bike1.display_info()

print(".................................................................................................................")

import math  # Needed for circle calculations

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area method.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Rectangle):  # Square is a type of Rectangle
    def __init__(self, side):
        super().__init__(side, side)

circle = Circle(7)
rectangle = Rectangle(10, 5)
square = Square(4)

print(f"Circle Area: {circle.area():.2f}")
print(f"Rectangle Area: {rectangle.area()}")
print(f"Square Area: {square.area()}")

print(".................................................................................................................")
