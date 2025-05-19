print("----------------------------ex.1------------------")

class Bankaccount:
    def __init__(self, balance, owner):
        self.__balance = balance
        self.owner = owner
        
    
    def get_balance (self, amount):
        if amount > 0:
            self.__balance += amount
        
        else: 
           print("Invalid amount")
    
    def deposit(Self ,amount):
        if amount >0 : 
            Self.__balance += amount
            print(f"Deposited ${amount}")
        
        else:
            print("amount cannot be less than zero")
        
    def withdraw(self, amount):
        if amount > self.__balance:
            print("error : insufficient balance")
        elif amount <= 0:
            print("Invalid amount")
        else: 
            self.__balance -= amount
            print(f"Withdrew : ${amount}")
    
    def display(self):
        print(f"Account owner: {self.owner}, Current balance: ${self.__balance}")

#test
account = Bankaccount(1000, "John")
account.display()

#depsoit money
account.deposit(500)
account.display()

#negative deposit 
account.deposit(-110)

#withdraw
account.withdraw(200)
account.display()

#over withdraw
account.withdraw(15000)

#setting new balance
account.get_balance(1000)
account.display()

#setting -ve balance
account.get_balance(-1234)
account.display()


print("----------------------------ex.2------------------")

class Temperature:
    def __init__(self, celsuis):
        self.__celsuis = celsuis

    def get_celsuis (self):
        return self.__celsuis

    def set_celsuis(self, value):
        if value >= -273.15 :
            self.__celsuis = value
        else:
            print("Invalid temperature")
    
    def to_fahrenheit(self):
        return (self.__celsuis * 9/5) + 32

    def show_temp(self):
        print(f"Temperature : {self.__celsuis} degree celsuis or {self.to_fahrenheit()}")

#test
t1 = Temperature(25)
t1.show_temp()

t1.set_celsuis(0)
t1.show_temp()

t1.set_celsuis(-288)

t1.set_celsuis(-100)

t1.show_temp()

print("current temperature: ", t1.get_celsuis())

print("----------------------------ex.3------------------")

class Employee:
    def __init__(self, name , salary):
        self.name = name
        self.__salary = salary
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, new_salary):
        if new_salary > self.__salary:
            print(f"The salary is raised from {self.__salary} to {new_salary}")
            self.__salary = new_salary
        else: 
            print("error: the new salary must be greater than old salary")

    def showInfo(self):
        print(f"Name: {self.name}, salary : {self.__salary}")

#test
e1 = Employee("Ram", 1234)
e1.showInfo()

e1.set_salary(123)
e1.showInfo()

e1.set_salary(123456)
e1.showInfo()

        
print("----------------------------Bonus------------------")

class LibraryBook:
    def __init__(self, title, author, is_borrowed= False):
        self.title = title
        self.author = author
        self.__is_borrowed = is_borrowed
    
    def borrow_book(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            print(f"You borrowed : '{self.title}'.")
        else: 
            print(f"'{self.title}' is already borrowed.")
    
    def return_book(self):
        self.__is_borrowed = False
        print(f"You returned '{self.title}' successfully.")
    
    def show_status(self):
        status = "Borrowed" if self.__is_borrowed else "Available"
        print(f"Book: '{self.title}' by {self.author} is {status}.")

#test
b = LibraryBook("Data Structures", "Narasimha Karumanchi")

b.show_status()
b.borrow_book()
b.show_status()
b.borrow_book()  # try borrowing again
b.return_book()
b.show_status()