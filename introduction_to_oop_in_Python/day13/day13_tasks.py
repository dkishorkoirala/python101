print("....................................................................................................................................")

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    
    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

a = Student("Hari",15, 10)
a.show_info()

print("....................................................................................................................................")

class Shape():
    def area(self):
        print(f"Calculating area ...")
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        print(f"Area of rectangle is : {self.length * self.width}")   

d = Rectangle(5, 6)
d.area()

print("....................................................................................................................................")

class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into {self.owner}'s account")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.owner}'s account")
        else:
            print(f"Insufficient balance in {self.owner}'s account")

    def display(self):
        print(f"Account holder: {self.owner}, Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def display(self):
        print(f"The account of {self.owner} with balance {self.balance} has interest rate {self.interest_rate}")

# Test
ac = SavingsAccount("Dibash", 1234123, "12%")
ac.display()
ac.deposit(5000)
ac.withdraw(2000)
ac.display()

print("....................................................................................................................................")