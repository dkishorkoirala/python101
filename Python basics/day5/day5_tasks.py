print(".................................task 1.......................................")

def greet_user():
    print("Welcome to the function")

greet_user()

print(".................................task 2.......................................")
def square(n):
    return n * n

SQ = square(n = int(input("Enter a to be square of: ")))
print("The square is : ", SQ)

print(".................................task 3.......................................")
def is_even(num):
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

check = is_even(num = int(input("Enter a number to be checked: ")))

print(".................................Challenge.......................................")

def calculator(a , b , op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error: Division by zero is not allowed"
        else:
            return a / b

operation = calculator( a = int(input("Enter the first number: ")), 
                       b = int(input("Enter the second number: ")), 
                       op = input("Enter the operation: "))
print("The result is: ", operation)

print("........................................................................")