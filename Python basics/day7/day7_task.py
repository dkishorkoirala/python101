print(".....................................................................")
book1= {
    "name" : "Rich dad, poor dad",
    "author" : "Robert Kiyosaki"
}
book2= {
    "name" : "The chemist",
    "author" : "Stephenie Meyer"
}
book3 = {
    "name" : "Bhagawat Geets",
    "author" : "Guru vyas"
}

print("Dictionary created of 3 favourite books")

print(".....................................................................")

fruits = {"banana", "apple", "mango","lichhi","graps"}
print(fruits)

print(".....................................................................")
contact = {}

while True:
    print("\n1. Add contact\n2. View Contact\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contact[name] = phone
        print(f"Contact {name} added successfully!")
    
    elif choice == "2":
        name = input("Enter name to search: ")
        if name in contact:
            print(f"Phone number of {name} is {contact[name]}")
        else:
            print("Contact not found!!!")
    elif choice == "3":
        break
    
    else:
        print("Invalid choice.")

print(".....................................................................")