print(".....................................................................")
def multiply(x , y):
    return x * y

i = float(input("Enter first for multiplication number: "))
j = float(input("Enter second for multiplication number: "))
result = multiply(i , j)
print("Product: ", result)

print(".....................................................................")

def division(a , b):
    try: 
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
        return None
    
n = float(input("Enter Numerator: "))
m = float(input("Enter Denominator: "))
result = division(n , m)
print("Division of Following Numbers are: ", result)

print(".....................................................................")

def add(x , y):
    return x + y

def sub(x , y):
    return x - y

def mul(x , y):
    return x * y

def div(x , y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
        return None

while True:
    print("1. Perform an Operation\n2. Exit")
    choice = input("Enter your Transaction: ")

    if choice == "1":
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
        operation = input("Enter your Operation: ")
        f = float(input("Enter first number: "))
        s = float(input("Enter second number: "))

        if operation == "1":
            print("Addition of Following Numbers are: ", add(f , s))

        elif operation == "2":
            print("Subtraction of Following Numbers are: ", sub(f , s))

        elif operation == "3":
            print("Multiplication of Following Numbers are: ", mul(f , s))
        
        elif operation == "4":
            print("Division of Following Numbers are: ", div(f , s))
    
    elif choice == "2":
        break
    
    else:
        print("Invalid Choice")
        
print(".....................................................................")
