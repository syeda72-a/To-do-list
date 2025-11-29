# To-Do List with Update Feature

tasks = []

while True:
    print("\n----- TO-DO LIST -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Update Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == '2':
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == '3':
        if not tasks:
            print("No tasks to delete.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            task_no = int(input("Enter task number to delete: "))
            if 1 <= task_no <= len(tasks):
                tasks.pop(task_no - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number!")

    elif choice == '4':
        if not tasks:
            print("No tasks to update.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

            task_no = int(input("Enter task number to update: "))
            if 1 <= task_no <= len(tasks):
                new_task = input("Enter updated task: ")
                tasks[task_no - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number!")

    elif choice == '5':
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1-5.")