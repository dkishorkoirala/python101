print("...............................................")

i = 1
while i <= 10:
    print(i)
    i += 1

print("...............................................")

for j in range(1, 21):
    if j % 2 == 0:
        print(j)

print("...............................................")

m = int (input("Enter the number you want multiplication table of : "))
for k in range(1, 11):
    print(f"{m} * {k} = {m*k}")

print("...............................................")

num = int(input("Enter any number: "))
sum = 0
for l in range(1, num+1):
    sum += l
    print("The sum of first", l, "Numbers is:", sum)

print("........................Challenge.......................")

number = int (input("Enter a number(between 1 to 50): "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)
print("...............................................")
