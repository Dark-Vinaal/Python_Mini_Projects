tasks = []

while True:
    print("=" * 30)
    print("***** TO-DO LIST *****")
    print("=" * 30)

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("*" * 30)

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        todo = input("Enter a new task: ")
        tasks.append(todo)
        print("Task ",todo," added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            print("Tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
            try:
                task_num = int(input("Enter the task number to delete : "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print("Task ",removed_task," deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("*" * 30)
        print("Exiting the program.")
        print("*" * 30)
        break

    else:
        print("Invalid choice. Please enter a number between 1 to 4...")