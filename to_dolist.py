def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['task']}")


tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter task: ")

        tasks.append({"task": task, "done": False})
        print("Task added successfully!")

    elif choice == "2":
        show_tasks(tasks)

    elif choice == "3":
        show_tasks(tasks)
        if tasks:
            try:
                task_num = int(input("Enter task number to mark as completed: "))
                tasks[task_num - 1]["done"] = True
                print("Task marked as completed!")
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "4":
        show_tasks(tasks)
        if tasks:
            try:
                task_num = int(input("Enter task number to delete: "))
                removed = tasks.pop(task_num - 1)
                print(f"Deleted task: {removed['task']}")
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
