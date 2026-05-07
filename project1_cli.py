#  TASK 1 : To-Do List Application using Python (CLI) 

tasks = []

def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def show_tasks():
    if not tasks:
        print("📝 No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "✅" if task['completed'] else "❌"
            print(f"{index}. {task['title']} - {status}")

def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "completed": False})
    print("✔️ Task added!")

def mark_completed():
    show_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]['completed'] = True
                print("✅ Task marked as completed!")
            else:
                print("⚠️ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a number.")

def delete_task():
    show_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"🗑️ Removed task: {removed['title']}")
            else:
                print("⚠️ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("👋 Exiting To-Do List App. Have a productive day!")
        break
    else:
        print("⚠️ Invalid choice. Please choose between 1-5.")
