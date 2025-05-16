print("...........................................................................................................")

class Car:
    def start_engine(self):
        print("Engine of car started")
    
class Bike:
    def start_engine(self):
        print("engine of bike started")

def start_any_vehicle(vehicle):
    vehicle.start_engine()

c = Car()
b = Bike()

start_any_vehicle(c)
start_any_vehicle(b)

print("...........................................................................................................")

class Employ:
    def __init__(self, salary):
        self.__salary = salary
    
    
    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
            print(f"Salary updated to: {self.__salary}")
        else:
            print("New salary must be greater than current salary.")

e = Employ(50000)
print("Current Salary:", e.get_salary())
e.set_salary(55000)  # Should update
e.set_salary(40000)  # Should NOT update

print("...........................................................................................................")

class Book:
    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.__availability = availability
    
    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"You have borrowed '{self.title}'.")
        else:
            print(f"'{self.title}' is currently not available.")

    def return_book(self):
        self.__availability = True
        print(f"You have returned '{self.title}'.")

    def show_info(self):
        status = "Available" if self.__availability else "Not Available"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")


b = Book("Python Mastery", "Alex Johnson", True)
b.show_info()
b.borrow_book()
b.show_info()
b.return_book()
b.show_info()
        
print("...........................................................................................................")
