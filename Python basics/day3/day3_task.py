print("................................................................")
num = int(input("enter a number : "))

if num < 0:
    print("Negative number")
elif num == 0:
    print("Zero")
else:
    print("Positive number")

print("................................................................")
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

print("................................................................")

age = int(input("Enter age: "))

if age < 13:
    print("You are a Child")
elif age >= 13 and age <= 19:
    print("You are a Tee")
else:
    print("You are an adult")

print(".................................challenge...............................")

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid Credentials")

print("................................................................")