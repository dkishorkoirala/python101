print("...........................................Task 1 ...........................................")

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def display(self):
        print(f"{self.owner} has {self.balance} in account")

#test
a1 = BankAccount("Radhey", 10000)
a1.display()

a2 = BankAccount("Shyam", 10000000)
a2.display()

print("...........................................Task 2 ...........................................")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def show_info(self):
        print(f"Reading {self.title} by {self.author}...")

#test
b1 = Book("Harry Potter", "J.K. Rowling")
b1.show_info()

b2 = Book("Rich Dad Poor Dad", "Robert Kiyosaki")
b2.show_info()

print("...........................................Task 2 ...........................................")

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    
    def details(self):
        print(f"This is a {self.brand} laptop that costs {self.price}.")
    
l1 = Laptop("Lenovo", 50000)
l1.details()

l2 = Laptop("Dell", 60000)
l2.details()