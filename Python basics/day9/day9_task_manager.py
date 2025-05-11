print("....................................Task Manager..............................................")
tasks = []

def show_menu():
    print("\n--Task Manager--")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice(1-5): ")

    if choice == "1":
        title = input("Enter task title: ")
        task = {"title" : title, "completed" : False}
        tasks.append(task)
        print(f"Task '{title}' added successfully!")

    elif choice == "2":
        if not tasks:
            print("No task found")
        else:
            print("\nYour Task: ")
            for idx, task in enumerate(tasks, start=1):
                status = "✔" if task["completed"] else "❌"
                print(f"{idx}. {task['title']} ({status})")

    
    elif choice == "3":
        num = int (input("Enter task number to mark as completed: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            print("Task marked as completed")
        else:
            print("Invalid task number.")
    
    elif choice == "4":
        num = int(input("Enter the task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Task '{removed['title']}' deleted successfully!")
        else: 
            print("Invalid task number.")
    
    elif choice == "5":
        print("Exiting Task Manager...")
        break
    
    else:
        print("Invalid choice. please try again...")