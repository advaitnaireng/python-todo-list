task_list = []

def show_menu():
    print("\n To-Do List App")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter a new task: ")
    task_list.append({"task" : task, "status" : False})
    print(f"Task '{task}' is added to the list.")

def show_tasks():
    if not task_list:
        print("You have nothing to do :)")
    else:
        print("\n Your Tasks:")
        for index, task in enumerate(task_list):
            status = "Complete" if task["status"] else "Incomplete"
            print(f"{index + 1}. {task['task']} - {status}")

def mark_task_complete():
    show_tasks()
    if not task_list:
        return
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        task_index = task_number - 1
        if task_index >= 0  and task_index < len(task_list):
            task_list[task_index]["status"] = True
            print(f"Task '{task_list[task_index]['task']}' is marked as complete.")
        else: print("Invalid task number.")

    except ValueError:
        print("Invalid number.")

def delete_task():
    show_tasks()
    if not task_list:
        return
    try:
        task_number = int(input("Enter the task number to delete: "))
        task_index = task_number - 1
        if task_index >= 0 and task_index < len(task_list):
            removed = task_list.pop(task_index)
            print(f"Task '{removed['task']}' is deleted from the list.")
        else: print("Invalid task number.")
    except ValueError:
        print("Invalid number.")

while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        mark_task_complete()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting the app. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
