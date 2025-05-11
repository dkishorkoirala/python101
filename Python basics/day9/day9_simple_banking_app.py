account = {
    "name" : "",
    "balance" : 0.0
}

def create_account():
    account["name"] = input("\nEnter account holder's name: ")
    account["balance"] = float(input("Enter initial balance: "))
    print(f"\nAccount created for {account['name']} with balance ${account['balance']}")

def check_balance():
    print(f"\nAccount holder name is {account['name']}")
    print(f"Current Balance: ${account['balance']}")

def deposit():
    amount = float(input("Enter amount to deposit: $"))
    if amount > 0:
        account["balance"] += amount
        print(f"\nDeposited ${amount}. New balance is ${account['balance']}")
    else:
        print("\nInvalid amount. Please enter a positive number.")

def withdrawl():
    amount = float(input("\nEnter amount to withdraw: $"))
    if amount <= account["balance"]:
        account["balance"] -= amount
        print(f"\nWithdrawn ${amount}. Remaining balance is ${account['balance']}")
    else: 
        print("\nInsufficient balance. Please try again.")

while True:
    print("\n........................Simple banking app........................")
    print("1. Create Account\n2. Check Balance\n3. Deposit\n4. Withdraw\n5. Exit")

    choice = input("\nEnter your Option: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        check_balance()
    elif choice == "3":
        deposit()
    elif choice == "4":
        withdrawl()
    elif choice == "5":
        print("\nExiting the app. .. ...\n")
        break
    else:
        print("\nInvalid option. Please try again.")